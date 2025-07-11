import boto3

s3 = boto3.resource('s3')
# bucket_name_create = 'my-new-bucket-devops-souvick2'
region = 'us-east-1'
file_name = "C:\IMPORTANT\PTHN_DEVOPS\s3.py"
# def create_bucket(s3,bucket_name_create,region):
#     bucket= s3.create_bucket(Bucket=bucket_name_create, CreateBucketConfiguration={'LocationConstraint': region})
#     print("Bucket created successfully", bucket.name)
# create_bucket(s3,bucket_name_create,region)

def get_s3(s3):
    # print(s3.buckets.all())
    for bucket in s3.buckets.all():
        print(bucket.name)
        print(bucket.creation_date)
get_s3(s3)


# create_bucket(s3)

bucket_name = ['my-new-bucket-devops-souvick2', 'my-new-bucket-devops-souvick']
# Delete the bucket
# def delete_s3_bucket(bucket_name):
#     for name in bucket_name:
#         bucket = s3.Bucket(name)
#         bucket.delete()
#         print(f"Bucket {name} deleted successfully.")
#     print(f"Bucket {bucket_name} deleted successfully.")



def empty_bucket(s3, bucket_name):
    try:
        for obj in s3.Bucket(bucket_name).objects.all():
            obj.delete()
        print(f"Bucket {bucket_name} emptied successfully.")
    except Exception as e:
        print(f"Error emptying bucket {bucket_name}: {e}")

# def delete_s3_bucket(bucket_name):
#     empty_bucket(s3, bucket_name)
#     bucket = s3.Bucket(bucket_name)
#     bucket.delete()
#     print(f"Bucket {bucket_name} deleted successfully.")
# delete_s3_bucket(bucket_name)

# delete bucket with try block and iterating thorugh all buckets
def delete_s3_bucket(bucket_name):
    try:
        empty_bucket(s3, bucket_name)
        bucket = s3.Bucket(bucket_name)
        bucket.delete()
        print(f"Bucket {bucket_name} deleted successfully.")
    except Exception as e:
        print(f"Error deleting bucket {bucket_name}: {e}")

for name in bucket_name:
    delete_s3_bucket(name)

#upload file to s3 bucket
# def upload_file_to_s3(s3,bucket_name_create,file_name,key_name):

#     data_inside_bucket= open(file_name, 'rb')
#     s3.Bucket(bucket_name_create).put_object(Key=key_name, Body=data_inside_bucket)
#     print("File uploaded successfully")
# upload_file_to_s3(s3, bucket_name_create, file_name, 's3_devops_code.tar.gz')
