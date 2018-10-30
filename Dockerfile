FROM python:2.7.15-stretch
MAINTAINER Justin Michalicek <justin.michalicek@mobelux.com>
RUN DEBIAN_FRONTEND=noninteractive apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-unauthenticated apt-transport-https
RUN DEBIAN_FRONTEND=noninteractive apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --allow-unauthenticated \
  inotify-tools \
  software-properties-common \
  sudo \
  vim \
  tree \
  && apt-get autoremove && apt-get clean

RUN useradd -m developer && echo "developer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER developer
ENV HOME=/home/developer PATH=/home/developer/.local/bin:$PATH
WORKDIR /home/developer/
# Specific versions of pip and pipenv for now due to a bug when both are at latest as of Oct 8. 2018
# https://github.com/pypa/pipenv/issues/2871#issuecomment-427336362
RUN sudo pip install pip==18.0 --upgrade
RUN pip install pipenv==2018.10.13 --user
RUN echo "export PATH=~/.local/bin:$PATH" >> ~/.bashrc
RUN echo "export PATH=~/.local/bin:$PATH" >> ~/.profile
ENV PIPENV_VENV_IN_PROJECT=1

expose 8000
