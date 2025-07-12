# Terraform AWS Infrastructure with Python & GitHub Actions

[![Terraform CI/CD](https://github.com/souvroy20/python-devops/actions/workflows/terraform.yml/badge.svg)](https://github.com/souvroy20/python-devops/actions/workflows/terraform.yml)
[![Manual Terraform Destroy](https://github.com/souvroy20/python-devops/actions/workflows/terraform-destroy.yml/badge.svg)](https://github.com/souvroy20/python-devops/actions/workflows/terraform-destroy.yml)

This project demonstrates a professional, automated approach to managing AWS infrastructure using Terraform, with the entire CI/CD process orchestrated by Python scripts and executed through GitHub Actions.

The goal is to provide a robust, secure, and maintainable template for Infrastructure as Code (IaC) that incorporates best practices like automated formatting, linting, security scanning, and a safe, manual-only destruction process.

---

## ✨ Features

- **Automated Infrastructure Deployment**: Deploys an AWS EC2 instance running an Apache web server.
- **Python Orchestration**: Uses clean, single-function Python scripts (`terraform_automate.py`, `terraform_destroy.py`) to execute a sequence of Terraform commands.
- **Robust CI/CD Pipeline**: Leverages GitHub Actions for a complete end-to-end workflow.
- **Automated Code Quality**:
  - **Formatting**: Automatically formats Terraform code (`terraform fmt`) on every run.
  - **Linting**: Uses **TFLint** with the AWS plugin to check for best-practice violations and potential errors.
- **Automated Security Scanning**:
  - **Static Analysis**: Uses **Checkov** to scan Terraform code for security misconfigurations.
  - **Persistent Reports**: Linter and security scan results (`tflint_results.txt`, `checkov_results.txt`) are automatically committed back to the repository for tracking.
- **Remote State Management**: Securely stores Terraform state in an **AWS S3 bucket** with state locking via **DynamoDB**.
- **Scheduled & Manual Triggers**: The deployment pipeline runs on push to `main`, on a nightly schedule, or can be triggered manually.
- **Gated Manual Destroy**: A separate, manual-only workflow with a confirmation step (`Type "destroy" to confirm`) to safely tear down all infrastructure.

---

## 📂 Project Structure

```
├── .github/
│   └── workflows/
│       ├── terraform.yml         # Main CI/CD pipeline for apply
│       └── terraform-destroy.yml # Manual workflow for destroy
├── terraform-project/
│   ├── .tflint.hcl             # TFLint configuration file
│   ├── backend.tf              # S3 remote state configuration
│   ├── ec2.tf                  # EC2 instance and Security Group resources
│   ├── outputs.tf              # Terraform outputs
│   ├── provider.tf             # AWS and TLS provider configuration
│   └── variables.tf            # Input variables
├── terraform_automate.py       # Python script to orchestrate deployment
├── terraform_destroy.py        # Python script to orchestrate destruction
├── checkov_results.txt         # Auto-generated security scan report
└── tflint_results.txt          # Auto-generated linter report
```

---

## 🚀 How It Works

This project is built around two distinct GitHub Actions workflows that use Python as the "glue" to execute a series of infrastructure management tasks.

### 1. The Deployment Pipeline (`terraform.yml`)

This is the primary workflow for building and maintaining the infrastructure. It is triggered automatically on a push to the `main` branch or on a nightly schedule.

The job follows these steps:

1.  **Checkout & Setup**: Checks out the code and sets up the required versions of Python and Terraform.
2.  **Configure Credentials**: Securely configures AWS credentials using GitHub Secrets.
3.  **Security Scan (Checkov)**: Scans the Terraform code for security vulnerabilities and saves the report.
4.  **Install Linter (TFLint)**: Installs the TFLint tool.
5.  **Run Automation Script**: Executes `terraform_automate.py`, which performs the following sequence:
    - `terraform fmt`: Ensures all code is formatted correctly.
    - `tflint`: Lints the code, saving results to `tflint_results.txt`. This is a "soft fail" and will not stop the pipeline.
    - `terraform init`: Initializes the backend and providers.
    - `terraform validate`: Validates the syntax of the Terraform files.
    - `terraform plan`: Creates an execution plan and saves it to a file.
    - `terraform apply`: Applies the saved plan, creating or updating the infrastructure.
6.  **Commit Results**: Commits the updated `checkov_results.txt` and `tflint_results.txt` files back to the repository, providing a persistent record of code quality and security posture.

### 2. The Destroy Pipeline (`terraform-destroy.yml`)

This workflow is designed for safety and is **manual-only**. It will never run automatically.

> **Warning:** This is a destructive action and will permanently delete the AWS resources managed by this project.

To execute it:

1.  Navigate to the **Actions** tab in the GitHub repository.
2.  Select the **Manual Terraform Destroy** workflow from the list.
3.  Click the **Run workflow** dropdown.
4.  In the `confirm_destroy` text box, type the word `destroy`.
5.  Click the **Run workflow** button.

The workflow will only proceed if the confirmation text is entered correctly. It then runs the `terraform_destroy.py` script, which initializes Terraform and executes `terraform destroy`.

---

## 📋 Prerequisites

To use this project in your own account, you will need:

1.  **An AWS Account**.
2.  **An S3 Bucket** for storing the Terraform remote state. Update the `bucket` name in `terraform-project/backend.tf`.
3.  **A DynamoDB Table** for state locking. Update the `dynamodb_table` name in `terraform-project/backend.tf`.
4.  **GitHub Secrets**: Configure the following secrets in your repository settings (`Settings` > `Secrets and variables` > `Actions`):
    - `AWS_ACCESS_KEY_ID`: Your AWS access key.
    - `AWS_SECRET_ACCESS_KEY`: Your AWS secret key.

---
