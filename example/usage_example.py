def usage_example(hostpath):
    import requests
    import requests_aws_iam_auth

    aws_access_key_id='AKIAIOSFODNN7EXAMPLE'
    aws_secret_access_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
    region_name='aws-example-region-1'

    auth = requests_aws_iam_auth.ApiGateway(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )

    requests.get("https://" + hostpath, auth=auth)
