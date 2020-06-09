from application import app
from flask import request, Response
from random import randint

@app.route('/animals', methods = ['GET', 'POST'])
def animals():
    animal = ['Rabbit', 'Tiger', 'Snake', 'Crocodile']
    return Response(animal[randint(0,3)], mimetype = 'text/plain')

 
