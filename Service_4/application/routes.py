@app.route('/disney_characterphrase', methods=['GET'])
def disney_characterphrase():
    name = requests.get('http://service2:5001/disney_characters')
    catchphrase = requests.get('http://service3:5002/marvel_catchphrase')
    response = 'Your random Character: ' + character.text + 'Random Alternative Catchphrase: ' + catchphrase.text
    return response

@app.route('/marvel_characterphrase', methods=['GET'])
def marvel_characterphrase():
    name = requests.get('http://service2:5001/marvel_characters')
    catchphrase = requests.get('http://service3:5002/disney_catchphrase')
    response = 'Your random Character: ' + character.text + 'Random Alternative Catchphrase: ' + catchphrase.text
    return response