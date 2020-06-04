from application import app
from flask import request, Response
@app.route('/characters/catchphrase', methods = ['GET', 'POST'])
def catchphrase():
    characters = request.data.decode('utf-8')
    if characters = 'Scooby Doo':
        catchphrase = 'Scooby Dooby Doo'

    elif characters = 'Homer Simpson':
        catchphrase = 'Doh'
    
    elif characters = 'Buzz Lightyear':
        catchphrase = 'To infinity and Beyond'

    elif characters = 'Fred Flinstone':
        catchphrase = 'Yabba Dabba Do'

    else:
        catchprase = 'No catchphrase found'

    return Response(catchphrase, mimetype='text/plain')
