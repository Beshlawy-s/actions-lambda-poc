import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Mohamed El-Beshlawy who is our DevOps Engineer')
    }
