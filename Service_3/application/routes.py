from application import app
from flask import request, Response

@app.route('/animals', methods = ['GET', 'POST'])
def animals():
    animal = ['Rabbit', 'Tiger', 'Snake', 'Crocodile']
    return Response(name[randint(0,3)], mimetype = 'text/plain')


@app.route('/mythical', methods = ['GET', 'POST'])
def mythical():
    species = ['Alien', 'Dragon', 'Fairy', 'Goblin']
    return Response(name[randint(0,3)], mimetype = 'text/plain')
 
