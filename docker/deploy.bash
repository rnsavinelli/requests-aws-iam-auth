VERSION=1

TAG=mateusamin/request-aws-iam-auth-build

docker build -f docker/build-dockerfile -t $TAG:latest -t $TAG:$CI_COMMIT_SHORT_SHA -t $TAG:$VERSION .

docker login --username mateusamincleardata --password $DOCKER_HUB_ACCESS_TOKEN

docker push $TAG:latest
docker push $TAG:$VERSION
docker push $TAG:$CI_COMMIT_SHORT_SHA