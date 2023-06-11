import requests
import pytest

token = 'd43cccfec485bb240aac9b4339f63971'
host = 'https://pokemonbattle.me:9104'
def test_status_code():
    answer = requests.post(f'{host}/pokemons', json=
                           {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers={'Content-Type' : 'application/json', 'trainer_token' : token})
    assert answer.status_code == 201

def test_trainers_code():
    answer_body = requests.get(f'{host}/trainers', params = {'trainer_id' : 4258})
    assert answer_body.json() ['trainer_name'] == 'Ё!!та' and answer_body.status_code == 200