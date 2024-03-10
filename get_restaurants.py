import requests

url = "https://api.yelp.com/v3/businesses/search?location=Tacoma&term=food&categories=%22burgers%22&sort_by=best_match&limit=20"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer 8aFMnycTG5WjzJ3hNlN6l_5vngRpSVRTf6rUPQwSGKlKxRKJhmq3EjdK6gZVADoVAS-7I6dkTQy7mA6vsLokW-1J-o05YhjMN-0Jjt06YBipO5OFuPA3r7siuBjuZXYx"
}

response = requests.get(url, headers=headers)

print(response.text)