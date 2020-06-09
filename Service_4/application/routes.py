from flask import render_template, request, redirect, Response
import requests
from application import app, db
from random import randint
from application.models import Disney, Marvel

@app.route('/full', methods=['GET', 'POST'])
def disney_full():
    beginning = requests.get('http://service_2:5001/disney')
    end = requests.get('http://service_3:5002/animals')
    response = beginning.text + ' ' + end.text
    

    disneycharacter= Disney(name= response)
    db.session.add(disneycharacter)
    db.session.commit()

    return response
