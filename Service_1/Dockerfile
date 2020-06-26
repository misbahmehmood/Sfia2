FROM python:latest

RUN mkdir /opt/service1/

COPY . /opt/service1/

WORKDIR /opt/service1/

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]


