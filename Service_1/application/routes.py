from flask import render_template, request, redirect, Response
import requests
from application import app, db
from application.models import Cartoon

@app.route('/', methods = ['GET'])
def home():
    cartoonData= Cartoon.query.all()
    response = requests.get('http://service_4:5003/full')
    result= response.text
    print(result)
    return render_template('home.html', cartooncharacter=cartoonData, result=result, title='Home')

