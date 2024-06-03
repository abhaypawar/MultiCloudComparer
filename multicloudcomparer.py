import click
import requests
import json
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Function to create a requests session with retries
def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

def get_gcp_cost(instance_type, region, usage_hours):
    url = f"https://cloudbilling.googleapis.com/v1/services/6F81-5844-456A/skus?key=Ag"
    
    try:
        session = requests_retry_session()
        response = session.get(url, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch GCP pricing data: {e}")
    
    data = response.json()
    for sku in data.get('skus', []):
        if sku['category']['resourceFamily'] == 'Compute' and instance_type in sku['description']:
            for pricing_info in sku['pricingInfo']:
                for rate in pricing_info['pricingExpression']['tieredRates']:
                    if 'nanos' in rate['unitPrice']:
                        price_per_hour = rate['unitPrice']['nanos'] / 1e9
                        return price_per_hour * float(usage_hours)
    
    return None  # Instance type not found or pricing information unavailable

def get_azure_cost(instance_type, region, usage_hours):
    url = f"https://prices.azure.com/api/retail/prices?$filter=serviceName eq 'Virtual Machines' and armRegionName eq '{region}' and skuName eq '{instance_type}'"
    
    try:
        session = requests_retry_session()
        response = session.get(url, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch Azure pricing data: {e}")
    
    data = response.json()
    for item in data['Items']:
        if item['skuName'] == instance_type and item['armRegionName'] == region:
            price_per_hour = float(item['unitPrice'])
            return price_per_hour * float(usage_hours)
    
    return None  # Instance type not found or pricing information unavailable

@click.command()
@click.option('--instance-type', prompt='Instance Type', help='Instance type (e.g., n1-standard-1)')
@click.option('--region', prompt='Region', help='Region (e.g., us-east1)')
@click.option('--usage-hours', prompt='Usage Hours', help='Number of hours the instance is utilized per month')
def compare_costs(instance_type, region, usage_hours):
    try:
        click.echo("Fetching GCP cost...")
        gcp_cost = get_gcp_cost(instance_type, region, usage_hours)
        
        click.echo("Fetching Azure cost...")
        azure_cost = get_azure_cost(instance_type, region, usage_hours)

        click.echo(f"GCP Cost: ${gcp_cost:.2f}" if gcp_cost else "GCP Cost: Not available")
        click.echo(f"Azure Cost: ${azure_cost:.2f}" if azure_cost else "Azure Cost: Not available")
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    compare_costs()

