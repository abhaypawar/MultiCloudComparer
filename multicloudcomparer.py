import click
import requests

def get_aws_cost(instance_type, region, usage_hours):
    url = f"https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/current/{region}/index.json"
    response = requests.get(url)
    data = response.json()

    for sku, details in data['products'].items():
        if details['attributes'].get('instanceType') == instance_type:
            price_dimensions = data['terms']['OnDemand'][sku]
            for term in price_dimensions.values():
                price_per_unit = term['priceDimensions'].values()
                for price in price_per_unit:
                    if price['unit'] == 'Hrs':
                        price_per_hour = float(price['pricePerUnit']['USD'])
                        return price_per_hour * float(usage_hours)

    return None  # Instance type not found or pricing information unavailable

def get_gcp_cost(instance_type, region, usage_hours):
    url = "https://cloudpricingcalculator.appspot.com/static/data/pricelist.json"
    response = requests.get(url)
    data = response.json()

    for sku, details in data.items():
        if sku.startswith('CP-COMPUTEENGINE-VMIMAGE-'):
            if details.get('regions'):
                if region in details['regions']:
                    price_per_hour = details['regions'][region].get('price', {}).get('USD')
                    if price_per_hour:
                        return float(price_per_hour) * float(usage_hours)

    return None  # Instance type not found or pricing information unavailable

def get_azure_cost(instance_type, region, usage_hours):
    url = f"https://prices.azure.com/api/retail/prices?$filter=serviceName eq 'Virtual Machines' and armRegionName eq '{region}' and skuName eq '{instance_type}'"
    response = requests.get(url)
    data = response.json()

    for item in data['Items']:
        if item['skuName'] == instance_type and item['armRegionName'] == region:
            price_per_hour = float(item['unitPrice'])
            return price_per_hour * float(usage_hours)

    return None  # Instance type not found or pricing information unavailable

@click.command()
@click.option('--instance-type', prompt='Instance Type', help='Instance type (e.g., t2.micro)')
@click.option('--region', prompt='Region', help='Region (e.g., us-east-1)')
@click.option('--usage-hours', prompt='Usage Hours', help='Number of hours the instance is utilized per month')
def compare_costs(instance_type, region, usage_hours):
    aws_cost = get_aws_cost(instance_type, region, usage_hours)
    gcp_cost = get_gcp_cost(instance_type, region, usage_hours)
    azure_cost = get_azure_cost(instance_type, region, usage_hours)

    click.echo(f"AWS Cost: ${aws_cost:.2f}" if aws_cost else "AWS Cost: Not available")
    click.echo(f"GCP Cost: ${gcp_cost:.2f}" if gcp_cost else "GCP Cost: Not available")
    click.echo(f"Azure Cost: ${azure_cost:.2f}" if azure_cost else "Azure Cost: Not available")

if __name__ == '__main__':
    compare_costs()
