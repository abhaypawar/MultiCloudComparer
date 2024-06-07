# MultiCloudComparer
MultiCloudComparer is a powerful CLI based tool designed to provide real-time cost comparisons for cloud instances across AWS, GCP, and Azure. Effortlessly input instance type, region, and usage hours to instantly retrieve and compare pricing, helping you make informed decisions and optimize your cloud spending.

# Cloud Cost Comparator CLI Tool: MultiCloudComparer 

## Overview
The Cloud Cost Comparator CLI Tool - MultiCloudComparer is a Python-based command-line interface (CLI) that allows users to compare the costs of using different cloud instances across AWS, GCP, and Azure. The tool fetches cost information from the respective cloud provider pricing APIs and provides a cost comparison based on user inputs such as instance type, region, and usage hours.

## Features
- Compare instance costs across AWS, GCP, and Azure
- Fetch real-time pricing information using cloud provider APIs
- Simple and intuitive CLI interface

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/abhaypawar/MultiCloudComparer.git
    cd MultiCloudComparer
    ```

2. Create a virtual environment and activate it (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the CLI tool with the following command:
```bash
python MultiCloudComparer.py --instance-type <INSTANCE_TYPE> --region <REGION> --usage-hours <USAGE_HOURS>

For Example: 
python MultiCloudComparer.py --instance-type t2.micro --region us-east-1 --usage-hours 100
```

## Sample Output
```
Example Output - text

Instance Type: t2.micro
Region: us-east-1
Usage Hours: 100
AWS Cost: $12.00
GCP Cost: $11.50
Azure Cost: $13.00
```

## Development

To contribute to the project, follow these steps:
```
    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Make your changes and commit them (git commit -am 'Add new feature').
    Push to the branch (git push origin feature-branch).
    Create a new Pull Request.
```

## Contributing

Contributions are welcome! Please read the CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.
License

This project is licensed under the Apache 2.0 License - see the LICENSE file for details.

## Acknowledgements

    Click for creating the CLI
    Requests for handling HTTP requests

## Contact

For any inquiries or feedback, please contact [asdpawar2024@gmail.com].
