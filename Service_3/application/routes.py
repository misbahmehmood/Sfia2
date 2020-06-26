from application import app
from flask import request, Response
from random import randint

@app.route('/profile', methods = ['GET', 'POST'])
def profile():
    information = ['Species', 'Catchphrase', 'TV show']
    return Response(information[randint(0,2)], mimetype = 'text/plain')

 
