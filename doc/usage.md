# Usage Guide

## Installation

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/MultiCloudComparer.git
    cd MultiCloudComparer
    ```

2. **Create a virtual environment and activate it (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Basic Usage

Run the CLI tool with the following command:
```bash
python cloud_cost_comparator.py --instance-type <INSTANCE_TYPE> --region <REGION> --usage-hours <USAGE_HOURS>
```
