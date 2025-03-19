import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url).json()
    print(f"{response['setup']}\n{response['punchline']}")

get_joke()
