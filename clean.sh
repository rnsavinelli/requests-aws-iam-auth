#!/bin/sh

rm -rf ./build/
rm -rf ./dist/
rm -rf ./requests_aws_iam_api_gateway.egg-info/

# If HOST_PATH is unset pytest will recreate the testing infrastructure. There maybe a better way to signal this.
unset HOST_PATH

pyclean .