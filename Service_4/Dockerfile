FROM python:latest

RUN mkdir /opt/Sfia2/

COPY . /opt/Sfia2/

WORKDIR /opt/Sfia2/

RUN pip3 install -r requirements.txt

EXPOSE 5003

ENTRYPOINT ["python3", "app.py"]

