import boto3
import logging
import botocore.exceptions

ACCESS_KEY = Access
SECRET_KEY = Key

class S3_Photo_Backup:
    def upload_file(filename, bucket, object_name=None):
        client = boto3.client('S3',aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = filename
        try:
            result = client.upload_file(file_name, bucket, object_name)
            print(filename + " uploaded successfully")
        except as e:
            logging.error(e)
            return False
        return True
#def send_email:



        


        

