# Face_Recognition_using_AWS_Services

# Face Recognition Using AWS Services
This project demonstrates how to create a face recognition system using AWS services such as Rekognition, S3, and DynamoDB. The system indexes faces, stores metadata, and recognizes faces in images.

# Prerequisites

# AWS Account: You need an AWS account to create and manage AWS services.

#AWS CLI: Install and configure the AWS CLI.

sh

pip install awscli
aws configure

Boto3: The AWS SDK for Python to interact with AWS services.

sh
pip install boto3

AWS Setup
Create Rekognition Collection

sh
aws rekognition create-collection --collection-id face_recognition_collection --region us-east-1

Create DynamoDB Table

sh
aws dynamodb create-table --table-name face_recognition \
--attribute-definitions AttributeName=RekognitionId,AttributeType=S \
--key-schema AttributeName=RekognitionId,KeyType=HASH \
--provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
--region us-east-1

Create S3 Bucket

sh
aws s3 mb s3://bucket-name --region us-east-1
