from flask import render_template, request, redirect, Response
import requests
from application import app, db
from random import randint
from application.models import Cartoon

@app.route('/full', methods=['GET', 'POST'])
def full():
    character = requests.get('http://service_2:5001/names').text
    profile = requests.get('http://service_3:5002/profile').text
    character=character
    
    if character == 'Homer Simpson':
        if profile == 'Species':
            fullprofile = Cartoon(
                name=character,
                information='Human',
                profiletype=profile
            )
            db.session.add(fullprofile)
            db.session.commit()
            
            return character + ':' + ' ' + ' Human'

        elif profile == 'TV show':
            fullprofile = Cartoon(
                name=character,
                information='The Simpsons',
                profiletype=profile
            )
            db.session.add(fullprofile)
            db.session.commit()
            
            return character + ':' + ' '  + ' The Simpsons'

        else:
            fullprofile = Cartoon(
                name=character,
                information='Doh!',
                profiletype=profile
            )
            db.session.add(fullprofile)
            db.session.commit()
            return character + ':' + ' '  + ' Doh'


    elif character == 'Scooby Doo':
        if profile == 'Species':
            fullprofile = Cartoon(
                name=character,
                information='Dog',
                profiletype=profile
            )
            db.session.add(fullprofile)
            db.session.commit()
            
            return character + ':' + ' '  + ' Dog'

        elif profile == 'TV show':
            fullprofile = Cartoon(
                name=character,
                information='Scooby-Doo, where are you!',
                profiletype=profile
            )
            db.session.add(fullprofile)
            db.session.commit()
            
            return character + ':' + ' '  + ' Scooby-Doo, where are you!'

        else: 
            fullprofile = Cartoon(
                name=character,
                information='Scooby Dooby Doo',
                profiletype=profile
            )
            db.session.add(fullprofile)
            db.session.commit()
            
            return character + ':' + ' ' + ' Scooby Dooby Doo'


    elif character == 'Buzz Lightyear':
        if profile == 'Species':
            fullprofile = Cartoon(
                name=character,
                information='Toy',
                profiletype=profile
            )
            db.session.add(fullprofile)
            db.session.commit()
            return character + ':' + ' ' +  ' Toy'

        elif profile == 'TV show':
            fullprofile = Cartoon(
                name=character,
                information='Toy Story',
                profiletype=profile
            )
            db.session.add(fullprofile)
            db.session.commit()
            
            return character + ':' + ' '  + ' Toy Story'

        else:
            fullprofile = Cartoon(
                name=character,
                information='To Infinity and Beyond',
                profiletype=profile
            )
            db.session.add(fullprofile)
            db.session.commit()
            return character + ':' + ' ' +  ' To infinity and Beyond'


    elif character == 'Tweety':
        if profile == 'Species':
            fullprofile = Cartoon(
                name=character,
                information='Bird',
                profiletype=profile
            )
            db.session.add(fullprofile)
            db.session.commit()
            return character + ':' + ' ' + ' Bird'

        elif profile == 'TV show':
            fullprofile = Cartoon(
                name=character,
                information='Looney Tunes',
                profiletype=profile
            )
            db.session.add(fullprofile)
            db.session.commit()
            
            return character + ':' + ' '  + ' Looney Tunes'

        else:
            fullprofile = Cartoon(
                name=character,
                information='I tawt I taw a puddy cat',
                profiletype=profile
            )
            db.session.add(fullprofile)
            db.session.commit()

            return character + ':' + ' ' + ' I tawt I taw a puddy cat'
    
    else:
        return 'No cartoons found'
            
    
    
