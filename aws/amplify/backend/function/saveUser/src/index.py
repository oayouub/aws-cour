import json
import os
import boto3
import uuid

def handler(event, context):

    body = json.loads(event['body'])

    table_name = os.environ['STORAGE_USERS_NAME']
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
    table = dynamodb.Table(table_name)

    table.put_item(
        Item={
            'id': str(uuid.uuid4()),
            'name': body['name'],
            'email': body['email']
        }
    )

    return {
        'statusCode': 200,
    }
