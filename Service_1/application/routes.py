from flask import render_template
from application import app

@app.route('/')
@app.route('/home')
def home():
    response = requests.get('http://service4:5003/characterphrase')
    print(response)
    characterphrase= response.text
    return render_template('home.html', characterphrase=characterphrase title='Home')

