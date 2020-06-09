FROM python:latest

RUN mkdir /opt/service1/

COPY . /opt/service1/

WORKDIR /opt/service1/

RUN apt-get update && apt install -y python3-pip

RUN apt-get install python3-venv -y

RUN python3 -m venv venv

RUN . venv/bin/activate

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]


