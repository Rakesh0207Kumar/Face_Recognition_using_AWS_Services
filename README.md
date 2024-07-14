

---

# Face Recognition Using AWS Services

This project demonstrates how to create a face recognition system using AWS services such as Rekognition, S3, and DynamoDB. The system indexes faces, stores metadata, and recognizes faces in images.

## Prerequisites

Before you begin, ensure you have the following:

1. **AWS Account**: You need an AWS account to create and manage AWS services.
2. **AWS CLI**: Install and configure the AWS CLI.
    ```sh
    pip install aws-shell
    aws configure
    ```
3. **Boto3**: The AWS SDK for Python to interact with AWS services.
    ```sh
    pip install boto3
    ```

## AWS Setup

Follow these steps to set up the required AWS services:

### 1. Create Rekognition Collection

Run the following command to create a Rekognition collection:

```sh
aws rekognition create-collection --collection-id face_recognition_collection --region us-east-1
```

### 2. Create DynamoDB Table

Run the following command to create a DynamoDB table:

```sh
aws dynamodb create-table --table-name face_recognition \
--attribute-definitions AttributeName=RekognitionId,AttributeType=S \
--key-schema AttributeName=RekognitionId,KeyType=HASH \
--provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
--region us-east-1
```

### 3. Create S3 Bucket

Run the following command to create an S3 bucket:

```sh
aws s3 mb s3://your-bucket-name --region us-east-1
```

Replace `your-bucket-name` with your desired S3 bucket name.

---

