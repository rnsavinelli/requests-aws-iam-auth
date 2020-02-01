#!/bin/sh

rm -rf ./build/
rm -rf ./dist/
rm -rf ./requests_aws_iam_api_gateway.egg-info/

unset HOST_PATH

pyclean .