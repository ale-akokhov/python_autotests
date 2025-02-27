import requests
import pytest

URL='https://api.pokemonbattle.ru/v2'
TOKEN='be7c06c46e9f266612b6cfa5eceb2bfc'
HEADER={'Content-Type':'application/json'}
TRAINER_ID=24504

def test_status_code():
    response_status_code=requests.get(url=f'{URL}/trainers', headers=HEADER)
    assert response_status_code.status_code==200

def test_trainer_name():
    response_trainer_name=requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID}, headers=HEADER)
    assert response_trainer_name.json()['data'][0]['trainer_name']=='Александр'