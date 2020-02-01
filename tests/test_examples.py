def test_example(hostpath):
    import requests
    import requests_aws_iam_api_gateway

    # Provide AWS creds and config per Boto3 specs: https://tknk.io/ri3v
    auth = requests_aws_iam_api_gateway.AuthAwsIamApiGateway()

    requests.get("https://" + hostpath, auth=auth)
