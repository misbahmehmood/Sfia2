FROM python:latest

RUN mkdir /opt/service3/

COPY . /opt/service3/

WORKDIR /opt/service3/

RUN apt-get update -y

RUN apt-get install python3-venv -y

RUN python3 -m venv venv

RUN . venv/bin/activate

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]