## Facial Recognition System – Step-by-Step Guide

### Step 1: Setting Up Infrastructure
🔹 1. Launch EC2 Instance
* Create an EC2 instance to act as your central compute environment.
* Choose an Amazon Machine Image (AMI), such as Ubuntu or Amazon Linux.
* Configure security groups to allow SSH access (port 22) and any necessary app ports (e.g., 80, 443).

🔹 2. Configure AWS CLI
* SSH into your EC2 instance.
* Install AWS CLI (if not pre-installed).

```bash
sudo apt install awscli  # For Ubuntu
aws configure
```
* Enter your AWS Access Key, Secret Key, default region, and output format.

🔹 3. Create AWS Rekognition Collection
* Use the CLI to create a Rekognition collection:

```bash
aws rekognition create-collection --collection-id face_collection
```
🔹 4. Clone GitHub Repository
* Clone the GitHub repo that contains your project files:

```bash

git clone https://github.com/your-repo-url.git
cd your-repo-directory
```

### Step 2: Configuring Core Components
🔹 5. Create S3 Bucket
* Create a bucket to store images:
```
bash

aws s3 mb s3://your-unique-bucket-name
```

* Set appropriate bucket policies for access.

🔹 6. Create DynamoDB Table
* Create a table to store metadata and face data:
```
bash
aws dynamodb create-table \
    --table-name FaceMetadata \
    --attribute-definitions AttributeName=FaceId,AttributeType=S \
    --key-schema AttributeName=FaceId,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
```
🔹 7. Create Lambda Function with S3 Trigger
* Write and deploy a Lambda function (Node.js or Python) that:
  * Gets triggered on S3 image upload.
  * Uses Rekognition to detect faces.
  * Stores results in DynamoDB.
* Attach the Lambda function to the S3 bucket using an event notification.

### Step 3: Implementing Facial Recognition
🔹 8. Upload Images to S3
* Upload an image using CLI or SDK:

```bash
aws s3 cp ./images/person1.jpg s3://your-bucket-name/
```
🔹 9. Generate Face Prints via Lambda
* Lambda gets triggered by the S3 upload.
* It:
  * Calls Rekognition to detect and index faces.
  * Stores face metadata and FaceId in DynamoDB.

🔹 10. Store Face Prints in DynamoDB
* The Lambda function writes face metadata (including FaceId, S3 location, etc.) into your DynamoDB table.

🔹 11. Deploy Web Application with Docker
* Use Docker to containerize your web app that:
    * Interfaces with S3, DynamoDB, and Rekognition.
    * Allows users to upload images and get matches.
```
bash

docker build -t facial-recognition-app .
docker run -p 80:80 facial-recognition-app
```
