## base image
FROM python:3.8.16

## update debian packages, python3 and anaconda
RUN apt-get update --fix-missing

# install causal impact
RUN pip3 install tfcausalimpact

## copy code
ADD runner.sh /
ADD src/. /src/
ADD main.py /

##make code executable in image
RUN chmod +x runner.sh
CMD script -c /runner.sh -a /home/output/terminal_log