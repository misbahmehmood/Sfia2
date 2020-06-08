from application import app
from flask import request, Response

@app.route('/disney/catchphrase', methods = ['GET', 'POST'])
def disney_catchphrase():
    catchphrase = ['To infinity and Beyond', 'Hakuna Matata', 'Just keep swimming', 'Off with their Heads']
    return Response[randint(character(0,3)], mimetype= 'text/plain')


@app.route('marvel/catchphrase', methods = ['GET', 'POST'])
def marvel_catchphrase():
    catchphrase = ['With great power comes great responsibility', 'Flame on', "I'm the best there is at what I do", 'Up, up and away']
    return Response[randint(character(0,3)], mimetype= 'text/plain')
 
