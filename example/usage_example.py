def test_example(hostpath):
    import requests
    import requests_aws_iam_auth



    auth = requests_aws_iam_auth.ApiGateway()

    requests.get("https://" + hostpath, auth=auth)
