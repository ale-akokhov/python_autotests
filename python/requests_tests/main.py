import requests

URL='https://api.pokemonbattle.ru/v2'
TOKEN='be7c06c46e9f266612b6cfa5eceb2bfc'
HEADER={'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create={
    "name": "Андрей",
    "photo_id": 48
}

response_create=requests.post(url=f'{URL}/pokemons', headers=HEADER, json= body_create)
print(response_create.text)

pokemon_id=response_create.json()['id']

body_change={
    "pokemon_id": pokemon_id,
    "name": "Стас",
    "photo_id": 48
}

response_change=requests.put(url=f'{URL}/pokemons', headers=HEADER, json= body_change)
print(response_change.text)

body_catch={
    "pokemon_id": pokemon_id
}

response_catch=requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json= body_change)
print(response_catch.text)

response_list=requests.get(url=f'{URL}/pokemons', headers=HEADER, params={'in_pokeball':1})

enemy_id=response_list.json()['data'][3]['id']

body_battle={
    "attacking_pokemon": pokemon_id,
    "defending_pokemon": enemy_id
}

response_battle=requests.post(url=f'{URL}/battle', headers=HEADER, json= body_battle)
print(response_battle.text)