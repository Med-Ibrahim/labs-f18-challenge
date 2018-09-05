from flask import Flask, render_template
import requests 
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/pokemon/<int:id>')
def getPokemon(id):
    url = "http://pokeapi.co/api/v2/pokemon/" + str(id)
    payload = ""
    response = requests.request("GET", url, data = payload)
    data = response.json()
    return "<h1> The pokemon with id " + str(id)+ " is "+data['name'] + "</h1>"

@app.route('/pokemon/<string:name>')
def getPokemonByName(name):
    url = "http://pokeapi.co/api/v2/pokemon/" + name
    payload = ""
    response = requests.request("GET", url, data = payload)
    data = response.json()
    return "<h1> " + name + " has id " + str(data['id']) + "</h1>" 

if __name__ == '__main__':
    app.run()
