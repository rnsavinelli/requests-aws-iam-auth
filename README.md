# Requests AWS IAM Auth
An AWS IAM authentication package for Requests. Supported services: API Gateway v1. This is intended for use in production environments at the 1.0 release.

## Usage example

### API Gateway v1
```python
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
```

## Developer Information

### Dependencies
Botocore, boto3.

### Headers
authorization, and x-amz-content-sha256 are directly modified in the signing protocal and will be set.

Expect for authorization, connection, expect, user-agent, x-amz-content-sha256, x-amz-security-token and x-amzn-trace-id all user set headers are signed.

If the user does not specify host it is derived and signed. 

If the method is not GET, HEAD, or OPTIONS, has a payload, and the user does not provide a content-length header it is derived and signed.

If there's a Date header, we set the date header. Otherwise, we set the X-Amz-Date header.

The underlying http.client will derive an unsigned accept-encoding header if not user specified.

If using STS x-amz-security-token will be set by this library.

### Payload
The payload is always signed using SHA 256.

### Protocols
HTTP and HTTPS 1.1 are supported.

## Contributor Notes
This library uses botocore for signing. 

Requests uses urllib3 which uses http.client.

Botocore relies on http.client deriving the host when absent. Botocore replicates this derivation and signs with it but does not append the header to the request to be sent. This has the potential for a mismatch error. There is a TODO in botocore to set the host header in the request.

### Copyright

Modified version of [Mateus Amin's requests-aws-iam-auth](https://github.com/MateusAmin/requests-aws-iam-auth) distributed under the same license.

### Modifications

api_gateway has been modified to make its implementation possible independently of your local aws configurations. 

This allows extended integration. For example, aws_access_key_id, aws_secret_access_key and region_name can now be variables extracted from a query performed against a database.

In any case, you can still configure your local aws settings under `~/.aws/config`, to later asign aws_access_key_id, aws_secret_access_key and region_name.
You can manually instantiate a botocore session object (assuming you use botocore) to extract those values. Eg.

```
>>> import botocore.session
>>> session = botocore.session.get_session()

>>> session.get_credentials().access_key
'AKIAIOSFODNN7EXAMPLE'

>>> session.get_credentials().secret_key
'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'

>>> session.get_config_variable('region')
'aws-example-region-1'
```

It is advisable to use the original version of this package if your use case involves using your local configuration.

### Contributors

All contributors can be found under the [insights/contributors](https://github.com/rnsavinelli/requests-aws-iam-auth/graphs/contributors) section.

### References
- https://github.com/jmenga/requests-aws-sign
- https://github.com/MateusAmin/requests-aws-iam-auth
- https://docs.python.org/3/library/http.client.html#module-http.client
- https://hg.python.org/cpython/file/3.2/Lib/http/client.py
- https://github.com/urllib3/urllib3/blob/063d888bc247eb6bd7aedcd32412bbb53c3c6ffb/src/urllib3/connection.py#L195
- https://github.com/psf/requests/blob/7b565d886c852609a849e79e4ad8f3f8fa8d8c23/requests/adapters.py#L166
