from application import app
from flask import Response
from random import randint

@app.route('/character/name', methods = ['GET'])
def characters():
    characters = ['Scooby Doo', 'Homer Simpson', 'Buzz Lightyear', 'Fred Flinstone']
    return Response[randint(character(0,3)], mimetype= 'text/plain')
    
