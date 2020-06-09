from flask import render_template, request, redirect, Response
import requests
from application import app, db
from application.models import Disney, Marvel

@app.route('/')
def disney_home():
    response = requests.get('http://service_4:5003/full')
    result= response.text
    disneycharacter= Disney(name= result)
    
    db.session.add(disneycharacter)
    db.session.commit()
    disneyData= Disney.query.all()

    return render_template('home.html', disneycharacter=disneyData, title='Home')

def marvel_home():
    response = requests.get('http://service_4:5003/marvel/full'),
    result= response.text
    marvelcharacter= Marvel(name= result)
    
    db.session.add(marvelcharacter)
    db.session.commit()
    marvelData=Marvel.query.all()

    return render_template('home.html', marvelcharacter=marvelData, title='Home')