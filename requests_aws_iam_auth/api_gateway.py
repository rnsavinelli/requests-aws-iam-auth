from boto3 import Session

from botocore.awsrequest import AWSRequest
from botocore.auth import SigV4Auth
from requests.auth import AuthBase
from requests import PreparedRequest


class ApiGateway(AuthBase):
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name) -> None:
        self.session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name,
        )


    def __call__(self, r: PreparedRequest) -> PreparedRequest:
        def getSignedRequest():
            signedRequest = AWSRequest(method=r.method.upper(),
                                       headers=r.headers,
                                       url=r.url,
                                       data=r.body)

            SigV4Auth(self.session.get_credentials(), 'execute-api',
                      self.session.region_name).add_auth(signedRequest)

            return signedRequest

        if 'connection' in r.headers:
            connection = r.headers['connection']
            del r.headers['connection']
            signedRequest = getSignedRequest()
            r.headers['connection'] = connection
            
        else:
            signedRequest = getSignedRequest()

        r.headers.update(signedRequest.headers)

        return r