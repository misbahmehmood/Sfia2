@app.route('/characterphrase', methods=['GET'])
def characterphrase():
    character = requests.get('http://service2:5001/characters')
    catchphrase = requests.get('http://service3:5002/catchphrase')
    response = 'Your random Character: ' + character.text + 'Random Catchphrase: ' + catchphrase.text
    return response
