import boto3
import os

# set the region and the name of the S3 bucket
REGION = 'us-east-1'

# Set your artifact path and bucket
bucket_name = 'my-s3-bucket'
artifact_path = '/path/to/my/artifact'

# create a connection to S3
s3 = boto3.client('s3', region_name='us-east-1')

# create a zip file of the backup
backup_file_name = os.path.basename(BACKUP_PATH) + '.zip'
os.system(f'zip -r {backup_file_name} {BACKUP_PATH}')

# upload the backup to S3
with open(artifact_path, 'rb') as data:
    s3.upload_fileobj(data, bucket_name, 'backup/artifact')

# delete the local backup file
os.remove(backup_file_name)