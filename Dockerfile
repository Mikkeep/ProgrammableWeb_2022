FROM slim-buster

RUN apt add --no-cache ansible

WORKDIR /code
COPY requirements.txt 
COPY website/ website/
COPY ansible/ ansible/
