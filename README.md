# AWS Cloud Engineering Scripts

This repository contains a collection of Python scripts designed to automate various tasks related to AWS cloud services. These scripts utilize the AWS SDK for Python (Boto3) to interact with different AWS resources, making it easier to manage cloud infrastructure programmatically.

## Scripts Overview

- **S3 Management** (`s3_management.py`):  
  Automate the management of Amazon S3 buckets and objects. This script includes functions for creating, listing, uploading, and deleting S3 buckets and objects.

- **DynamoDB Operations** (`dynamodb_operations.py`):  
  Perform CRUD (Create, Read, Update, Delete) operations on DynamoDB tables. This script demonstrates how to create a table, add items, query data, and delete tables.

- **SQS and SNS Messaging** (`sqs_sns_messaging.py`):  
  Manage Amazon SQS (Simple Queue Service) and SNS (Simple Notification Service) for messaging between distributed systems. This script includes examples of sending messages to SQS queues, receiving messages, and publishing notifications via SNS.

- **Secrets and Encryption Management** (`kms_secrets_management.py`):  
  Handle sensitive data using AWS KMS (Key Management Service), Secrets Manager, and SSM (Systems Manager) Parameter Store. This script demonstrates how to create encryption keys, encrypt and decrypt data, and securely store secrets.

## Prerequisites

Before running these scripts, ensure that you have:

1. **Python 3.x** installed on your system.
2. **Boto3** installed via pip:
   ```bash
   pip install boto3
3. AWS credentials configured on your machine. You can set them up using the AWS CLI:
   ```bash
   aws configure

## Usage

These scripts can be converted into bash and run directly from the terminal.
