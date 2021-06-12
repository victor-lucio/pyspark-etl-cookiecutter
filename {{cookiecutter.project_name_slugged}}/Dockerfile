FROM ubuntu:16.04

RUN apt-get update && \
    apt-get upgrade -y
    
RUN apt-get install -q -y openjdk-8-jdk
RUN apt-get install -y python3.9.5

COPY . /{{cookiecutter.project_name_slugged}}

RUN cd /{{cookiecutter.project_name_slugged}} && \
    pip3 install -r requirements.txt && \
    pip3 install .

# workdir
WORKDIR /{{cookiecutter.project_name_slugged}}
CMD ["bash"]
