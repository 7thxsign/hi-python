import requests

base_url = "https://pokeapi.co/api/v2/"

def get_info_pokemon(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Pokemon {name} not found ({response.status_code})")

pokemon_name = "typhlosion"
pokemon_info = get_info_pokemon(pokemon_name)
pokemon_info = get_info_pokemon(pokemon_name)

if pokemon_info:
    print(f"{pokemon_info["name"]}")
    print(f"{pokemon_info["id"]}")
    print(f"{pokemon_info["height"]}")
    print(f"{pokemon_info["weight"]}")