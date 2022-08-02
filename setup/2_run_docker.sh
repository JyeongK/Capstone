#!/bin/bash
SETUP_PATH=`pwd -P`
cd ../RDS
PROJ_PATH=`pwd -P`	# project path
CONTAINER_NAME=rds_test
AVAILABLE_GPUS=0		# 0,1,2,3번 GPU 사용

sudo NV_GPU=${AVAILABLE_GPUS} nvidia-docker run \
    -it \
    --userns=host \
    --net=host \
    --ipc=host \
    --privileged \
    --user $(id -u ${USER}):$(id -g ${USER}) \
    -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY \
    -v /etc/passwd:/etc/passwd:ro \
    -v /etc/group:/etc/group:ro \
    -v /run/user/1000:/run/user/1000 \
    -v /dev:/dev \
    -v ${PROJ_PATH}:/home/${USER}/RDS \
    -v ${SETUP_PATH}:/home/${USER}/setup \
    -e DOCKER_CONTAINER_NAME=${CONTAINER_NAME} \
    -e PS1="🐳 \e[0;34m ${CONTAINER_NAME}[\u@\h]: \e[0m\w\$ " \
    --name ${CONTAINER_NAME} rds_test 
cd setup
