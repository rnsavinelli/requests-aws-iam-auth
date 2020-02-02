import boto3  # type: ignore
import os
import pytest  # type: ignore


@pytest.fixture(scope="session")
def init():
    if 'HOST_PATH' in os.environ:
        return

    client = boto3.client('apigateway')
    get_rest_apis_response = client.get_rest_apis()

    for item in get_rest_apis_response['items']:
        if item['name'] == 'TESTING_INFRASTRUCTURE':
            response = client.delete_rest_api(restApiId=item['id'])

    create_rest_api_response = client.create_rest_api(
        name='TESTING_INFRASTRUCTURE',
        description='TESTING_INFRASTRUCTURE',
        version='1',
        binaryMediaTypes=[
            'string',
        ],
        endpointConfiguration={'types': [
            'EDGE',
        ]},
        tags={'TESTING_INFRASTRUCTURE': 'TESTING_INFRASTRUCTURE'},
    )

    get_resources_response = client.get_resources(
        restApiId=create_rest_api_response['id'], limit=1)

    put_method_response = client.put_method(
        restApiId=create_rest_api_response['id'],
        resourceId=get_resources_response['items'][0]['id'],
        httpMethod='ANY',
        authorizationType='AWS_IAM',
        operationName='string')

    response = client.put_method_response(
        restApiId=create_rest_api_response['id'],
        resourceId=get_resources_response['items'][0]['id'],
        httpMethod='ANY',
        statusCode='200')

    put_integration_response = client.put_integration(
        restApiId=create_rest_api_response['id'],
        resourceId=get_resources_response['items'][0]['id'],
        httpMethod='ANY',
        type='MOCK',
        requestTemplates={
            'application/json':
            '''{
                #if( $input.params('content-type') == "application/json" )
                    "statusCode": 200
                #else
                    "statusCode": 500
                #end
            }'''
        })

    response = client.put_integration_response(
        restApiId=create_rest_api_response['id'],
        resourceId=get_resources_response['items'][0]['id'],
        httpMethod='ANY',
        statusCode='200',
        selectionPattern='')

    invoke_method_response = client.test_invoke_method(
        restApiId=create_rest_api_response['id'],
        resourceId=get_resources_response['items'][0]['id'],
        httpMethod='GET')

    stageName = 's'
    create_deployment_response = client.create_deployment(
        restApiId=create_rest_api_response['id'], stageName=stageName)

    os.environ['HOST_PATH'] = create_rest_api_response[
        'id'] + '.execute-api.' + boto3.Session(
        ).region_name + '.amazonaws.com/' + stageName + '/'


@pytest.fixture()
def hostpath(init):
    return os.environ['HOST_PATH']