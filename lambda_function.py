import boto3
import json


s3_client = boto3.client('s3') #Create S3 client object
dynamodb = boto3.resource('dynamodb') #Create dynamodb resource object

def lambda_handler(event, context):
    #assign s3 bucket name to a variable
    bucket_name = event['Records'][0]['s3']['bucket']['name'] 

    #assign s3 object name to a variable
    file_name = event['Records'][0]['s3']['object']['key']
    #print('Bucket Name :',bucket_name)
    #print('File Name :', file_name)
    
    #Get and assing s3 object to a variable
    json_object=s3_client.get_object(Bucket=bucket_name, Key=file_name)
    
    #parse Json file assing only Body to json_reader
    json_reader = json_object['Body'].read()

    jsonDict = json.loads(json_reader)
    
    #assing DynamoDB 'employee' table to table variable
    table = dynamodb.Table('employee')
    
    #populate json file to DynamoDB table
    table.put_item(Item=jsonDict)
        