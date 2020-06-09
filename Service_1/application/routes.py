from flask import render_template, request, redirect, Response
import requests
from application import app, db
from application.models import Disney, Marvel

@app.route('/', methods = ['GET'])
def disney_home():
    disneyData= Disney.query.all()
    response = requests.get('http://service_4:5003/full')
    result= response.text
    print(result)
    return render_template('home.html', disneycharacter=disneyData, result=result, title='Home')
