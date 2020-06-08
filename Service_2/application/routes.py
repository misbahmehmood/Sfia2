from application import app
from flask import Response
from random import randint

@app.route('/disney/name', methods = ['GET', 'POST'])
def disney_characters():
    name = ['Mickey Mouse', 'Goofy', 'Maleficent', 'Woody']
    return Response[randint(name(0,3)], mimetype= 'text/plain')


@app.route('marvel/name', methods = ['GET', 'POST'])
def marvel_characters():
    name = ['Spider-Man', 'Deadpool', 'Jessica Jones', 'Hulk']
    return Response[randint(name(0,3)], mimetype= 'text/plain')