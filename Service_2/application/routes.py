from application import app
from flask import Response
from random import randint

@app.route('/names', methods = ['GET', 'POST'])
def names():
    name = ['Homer Simpson', 'Scooby Doo', 'Buzz Lightyear', 'Tweety']

    return Response(name[randint(0,3)], mimetype = 'text/plain')
