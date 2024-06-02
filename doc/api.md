# API Documentation

## AWS Pricing API

### Endpoint
```
https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/current/{region}/index.json

### Description

This endpoint provides pricing information for AWS EC2 instances in the specified region.

### Example

```python
def get_aws_cost(instance_type, region, usage_hours):
    url = f"https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/current/{region}/index.json"
    response = requests.get(url)
    data = response.json()
    # Process the pricing information
```

## GCP Pricing API

### Endpoint

```
https://cloudpricingcalculator.appspot.com/static/data/pricelist.json

Description

This endpoint provides pricing information for Google Cloud Platform instances.
Example

python

def get_gcp_cost(instance_type, region, usage_hours):
    url = "https://cloudpricingcalculator.appspot.com/static/data/pricelist.json"
    response = requests.get(url)
    data = response.json()
    # Process the pricing information
```

## Azure Pricing API

### Endpoint

```
https://prices.azure.com/api/retail/prices?$filter=serviceName eq 'Virtual Machines' and armRegionName eq '{region}' and skuName eq '{instance_type}'

Description

This endpoint provides pricing information for Azure Virtual Machines in the specified region.
Example

python

def get_azure_cost(instance_type, region, usage_hours):
    url = f"https://prices.azure.com/api/retail/prices?$filter=serviceName eq 'Virtual Machines' and armRegionName eq '{region}' and skuName eq '{instance_type}'"
    response = requests.get(url)
    data = response.json()
    # Process the pricing information
```

## Error Handling

Ensure to handle errors gracefully, such as when the instance type or region is not found. You can return a None or a suitable message indicating the unavailability of pricing information.

### Additional Resources
```
For more detailed information on the APIs used, refer to the official documentation of AWS, GCP, and Azure pricing APIs.
```

This `api.md` file provides documentation for the APIs used in your project, including endpoints, descriptions, examples, and error handling information.
