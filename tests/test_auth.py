import os
import pytest  # type: ignore
import requests
import requests_aws_iam_api_gateway


@pytest.fixture()
def s():
    os.environ['AWS_PROFILE'] = 'juno-dev'
    s = requests.Session()
    s.auth = requests_aws_iam_api_gateway.AuthAwsIamApiGateway()
    return s


# @pytest.fixture()
# def s():
#     from requests_aws_sign import AWSV4Sign
#     from boto3 import session

#     os.environ['AWS_PROFILE'] = 'juno-dev'
#     session = session.Session()
#     s = requests.Session()
#     s.auth = AWSV4Sign(session.get_credentials(), session.region_name,
#                        'execute-api')
#     return s


@pytest.fixture()
def sf():
    if 'AWS_PROFILE' in os.environ:
        del os.environ['AWS_PROFILE']
    s = requests.Session()
    s.auth = requests_aws_iam_api_gateway.AuthAwsIamApiGateway()
    return s


def build_url(scheme, hostpath):
    return scheme + '://' + hostpath


def test_content_type_pass(hostpath, s):
    url = build_url('https', hostpath)
    headers = {'content-type': 'application/json'}

    r = s.options(url, headers=headers)
    assert 200 == r.status_code


def test_content_type_fail(hostpath, s):
    url = build_url('https', hostpath)
    headers = {'content-type': 'application/text'}

    r = s.options(url, headers=headers)
    assert 500 == r.status_code


def test_v1_http_auth_pass(hostpath, s):
    url = build_url('http', hostpath)

    r = s.options(url)
    assert 200 == r.status_code


def test_v1_https_auth_pass(hostpath, s):
    url = build_url('https', hostpath)

    r = s.options(url)
    assert 200 == r.status_code


def test_v1_http_auth_fail(hostpath, sf):
    url = build_url('http', hostpath)

    r = sf.options(url)
    assert 403 == r.status_code


def test_v1_https_auth_fail(hostpath, sf):
    url = build_url('https', hostpath)

    r = sf.options(url)
    assert 403 == r.status_code
