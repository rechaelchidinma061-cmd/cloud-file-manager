import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "chidinma-file-manager-2026-0811"
s3 = boto3.client("s3") 

def upload_file(filename):
    try:
        s3.upload_file(filename, BUCKET_NAME, filename)
        print("file uploaded to Amazon S3 successfully.")

    except FileNotFoundError:
        print("Error: The local file was not found.")

    except ClientError as e:
        print("Error uploading file to s3:", e)

def list_files():
    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME)

        if "Contents" in response:
            print("files stored in Amazon s3:")

            for item in response["Contents"]:
                print("-", item["Key"])

        else:
            print("Your s3 bucket is empty.")

    except ClientError as e:
        print("Error listing files in s3:", e)

def delete_file(filename):
    try:
        s3.delete_object(Bucket=BUCKET_NAME, Key=filename)
        print("file deleted from Amazon S3 successfully!")

    except ClientError as e:
        print("Error deleting file from s3:", e)

def download_file(filename):
    try:
        s3.download_file(BUCKET_NAME, filename, filename)
        print("file downloaded from Amazon S3 successfully!")

    except ClientError as e:
        print("Error downloading file from s3:", e)