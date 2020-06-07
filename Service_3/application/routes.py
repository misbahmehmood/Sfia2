from application import app
from flask import request, Response
@app.route('/characters/catchphrase', methods = ['GET', 'POST'])
def catchphrase():
    catchphrase = ['Scooby Dooby Doo', 'Doh', 'To infinity and Beyond', 'Yabba Dabba Do']
    
    return Response[randint(character(0,3)], mimetype= 'text/plain')
 
