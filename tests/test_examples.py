def test_example(hostpath):
    import requests
    import requests_aws_iam_auth

    # Provide AWS creds and config per Boto3 specs: https://tknk.io/ri3v
    auth = requests_aws_iam_auth.ApiGateway()

    requests.get("https://" + hostpath, auth=auth)
