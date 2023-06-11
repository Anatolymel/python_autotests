import requests
token = 'd43cccfec485bb240aac9b4339f63971'
answer = requests.post('https://pokemonbattle.me:9104/pokemons', json = {"name": "loki", "photo": "https://dolnikov.ru/pokemons/albums/001.png"},
                        headers = {"Content-Type" : "application/json", 'trainer_token': token})
print(answer.text)

answer = requests.put('https://pokemonbattle.me:9104/pokemons', json = {"pokemon_id": "13180","name": "loooook","photo": "https://dolnikov.ru/pokemons/albums/007.png"},
                       headers = {"Content-Type" : "application/json", 'trainer_token': token})
print(answer.text)

answer = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', json = {"pokemon_id": "12650"},
                       headers = {"Content-Type" : "application/json", 'trainer_token': token})
print(answer.text)