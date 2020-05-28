# S3_Photo_Backup
-------
# Process
1. In your AWS CLI, type:
```aws cloudformation create-stack --stack-name <Your Stack Name> --template-body file://Infra/S3_CF.yml --parameters ParameterKey=BucketName,ParameterValue=<Your BucketName> ParameterKey=UserNameParameterValue=e<Your IAM User Name> --capabilities CAPABILITY_NAMED_IAM```
