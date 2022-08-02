#!/bin/bash
CONTAINER_NAME=rds_test
sudo docker build --build-arg USER_NAME=${USER} -t rds_test .


# 여기서 .은 현재 폴더내의 모든 프로젝트를 포함하겠다는 의미이므로 처음 빌드 시간이 길어질 수 있음. (참고)
