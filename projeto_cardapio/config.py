import json

with open('projeto_cardapio/credentials.json') as file_json:
    config = json.load(file_json)

MY_SECRET_KEY = config.get('SECRET_KEY')
ENGINE = config.get('ENGINE')
NAME = config.get('NAME')
USER = config.get('USER')
PASSWORD = config.get('PASSWORD')
HOST = config.get('HOST')
PORT = config.get('PORT')