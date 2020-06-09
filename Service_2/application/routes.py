from application import app
from flask import Response
from random import randint

@app.route('/disney', methods = ['GET', 'POST'])
def disney_beginning():
    name = ['Mickey', 'Minnie', 'Donald', 'Tinker']
    return Response(name[randint(0,3)], mimetype = 'text/plain')


@app.route('/marvel', methods = ['GET', 'POST'])
def marvel_beginning():
    name = ['Super', 'Spider', 'Iron', 'Wonder']
    return Response(name[randint(0,3)], mimetype = 'text/plain')