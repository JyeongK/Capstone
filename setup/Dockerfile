# set basedockerfile
# [by Joungil Yun] ETRI와 동일한 cuda, cudnn 버전으로 수
FROM nvidia/cuda:11.3.0-cudnn8-devel-ubuntu18.04
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# install required packages (python)

# [by Joungil Yun] 일부 패키지 수정
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get install -y sudo apt-utils    

RUN apt-get install -y wget python-pip python-dev build-essential checkinstall && \
    apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev && \
    apt-get install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev wget libbz2-dev liblzma-dev && \
    apt-get install -y git && \
    pip install --upgrade pip

RUN apt-get install -y cmake protobuf-compiler python-pil python-lxml

# [by Joungil Yun] python 3.7.x 하위 버전은 크게 문제되지 않아 컴파일 대신 기본 패키지로 설치
RUN apt-get install -y python3 python3-pip python3-dev python3-setuptools
RUN pip3 install --upgrade pip
RUN apt-get install -y python3.7-dev python3.7-venv python3.7-tk
RUN apt-get install -y python3.8-dev python3.8-venv python3.8-tk

##############################################################################################################
# [by Joungil Yun] host와 docker 간의 공유 폴더, 파일의 권한 문제가 없도록 root로 사용 지양 (현재 user 환경으로 설정)
## user 계정 환경 및 권한 설정
# docker image build과정에서 user명으로 설정됨
ARG USER_NAME

RUN adduser --disabled-password --gecos '' ${USER_NAME} \
 && adduser ${USER_NAME} sudo \
 && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER ${USER_NAME}

RUN echo "export PS1='🐳 \e[0;34m$DOCKER_CONTAINER_NAME [\u@\h]: \e[0m\W$ '" >> ~/.bashrc
#RUN echo "PS1='🐳 \e[0;34m$DOCKER_CONTAINER_NAME [\u@\h]: \e[0m\W$ '" >> ~/.bashrc

ENV HOME /home/${USER_NAME}

WORKDIR /home/${USER_NAME}

#RUN echo 'export PS1="🐳 \e[0;34m$DOCKER_CONTAINER_NAME [\u@\h]: \e[0m\W$ "' > ~/.profile


#RUN echo "alias python=python3" >> ~/.bashrc

##############################################################################################################

CMD ["/bin/bash"]
#CMD ["export PS1='🐳 \e[0;34m$DOCKER_CONTAINER_NAME [\u@\h]: \e[0m\W$ '"]
