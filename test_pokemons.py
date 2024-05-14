import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
token = '0878e14f46a6f5569abf68f09146ed55'
Header = {'Content-Type' : 'application/json', 'trainer_token': token}
TRAINER_ID = '2628'
def test_status_code(): 
    responce = requests.get(url = f'{URL}/pokemons',params = {'trainer_id':TRAINER_ID})
    assert responce.status_code == 200

def test_part_of_responce():
    responce_get = requests.get(url = f'{URL}/pokemons',params = {'trainer_id':TRAINER_ID})
    assert responce_get.json()['data'][0]['name'] == 'Бульбазавр'
    
@pytest.mark.parametrize('key, value',[('name', 'Бульбазавр'), ('trainer_id', TRAINER_ID), ('id', '27368')])
def test_parametrize(key, value):
    responce_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id':TRAINER_ID})
    assert responce_parametrize.json()['data'][0][key] == value