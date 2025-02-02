import requests

def get_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}  # Important: Set the Accept header
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() #check for errors
        joke_data = response.json()
        joke = joke_data["joke"]
        return joke
    except requests.exceptions.RequestException as e:
        return f"Error getting a joke: {e}"

