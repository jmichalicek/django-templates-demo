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

# Copy Pipfile and Pipfile.lock and install deps first so that hopefully they are more likely to be
# in the docker layer cache already
RUN mkdir code
RUN mkdir code/demo/
COPY --chown=developer ./Pipfile ./Pipfile.lock /home/developer/code/
WORKDIR /home/developer/code
RUN PATH=~/.local/bin:$PATH pipenv install --ignore-pipfile --deploy

# Now copy everything so that we get all of our code, etc.
WORKDIR /home/developer/
COPY --chown=developer . /home/developer/code/
WORKDIR /home/developer/code

expose 8000

# May want to make this bash -ic 'foo' to enforce interactive shell
# TODO: May need to start up nvm here first
# ENTRYPOINT ['/bin/sh', '-c']
CMD bash -c 'pipenv run python manage.py runserver 0.0.0.0:8000'
