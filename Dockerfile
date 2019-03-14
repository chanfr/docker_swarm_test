FROM ubuntu:16.04

RUN apt-get update && apt-get upgrade -y
RUN useradd -ms /bin/bash docker && echo docker:docker | chpasswd
RUN apt-get install -y python-pip
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN  pip install -r requirements.txt
WORKDIR  /home/docker/
RUN  mkdir /home/docker/devel
COPY main.py devel/main.py
RUN ls
CMD python devel/main.py
