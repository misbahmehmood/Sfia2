FROM python:latest

RUN mkdir /opt/secondproject/

COPY ./opt/secondproject/

WORKDIR /opt/secondproject/

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]


