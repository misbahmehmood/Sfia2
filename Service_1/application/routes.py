from flask import render_template
from application import app, db
from application.models import Disney, Marvel

@app.route('/')
@app.route('/disney')
def home():
    data=Disney(
    response = requests.get('http://service_4:5003/disney_characterphrase'),
    characterphrase= response.text)
    
    db.session.add(characterphrase)
    db.session.commit()

    return render_template('home.html', characterphrase=characterphrase, title='Home')

@app.route('/marvel')
def home():
    data=Marvel(
    response = requests.get('http://service_4:5003/marvel_characterphrase'),
    characterphrase= response.text)
    
    db.session.add(characterphrase)
    db.session.commit()

    return render_template('home.html', characterphrase=characterphrase, title='Home')