from flask import render_template, request, redirect, Response
import requests
from application import app

@app.route('/full', methods=['GET'])
def disney_full():
    beginning = requests.get('http://service2:5001/disney')
    end = requests.get('http://service3:5002/animals')
    response = beginning.text + ' ' + end.text
    return response

@app.route('/marvel/full', methods=['GET'])
def marvel_full():
    beginning = requests.get('http://service2:5001/marvel')
    end = requests.get('http://service3:5002/mythical')
    response = beginning.text + ' ' + end.text
    return response