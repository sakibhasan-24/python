import requests

base_url=""


def get_pokemon(pokemon_name):
    url=base_url+"pokemon/"+pokemon_name
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        print(data["name"])
        print(data["height"])
        print(data["weight"])
        print(data["abilities"])
    else:
        print("Invalid pokemon name")


name=input("Enter a pokemon name: ")
get_pokemon(name)