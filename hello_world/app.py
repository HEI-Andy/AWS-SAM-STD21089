import json

# import requests


def lambda_handler(event, context):
     
    a = int(event['queryStringParameters']['a'])
    b = int(event['queryStringParameters']['b'])
    result = a + b
    response = {
        'statusCode': 200,
        'body': str(result)
    }
    return response;
