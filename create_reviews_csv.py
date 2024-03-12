import csv

import requests

business_ids = [
    "yD8fH2xeUzURUM8qMGbzHw",
    "xZnlRzauK2oUSl4v2rHPDQ",
    "37Pd-RvjfhmzZNQ2nK1WRA",
    "HurE9y2vT6rvkJnMq3MUug",
    "gLY9r32Vf4wUhLfDN4xZqw",
    "RfBkkXicWuTTeBQMyFBfCQ",
    "nP7wr9Ns4TnAub5GM-anGA",
    "KGOncoGpvrzGI4kDC1oXSw",
    "bUBiBh6HRV--sbX5DAYYUg",
    "qR3b6jaMzrdlj4jLDAohnw",
    "SvpZFYnWANObpJW6MTEZig",
    "jLAnkmyrAzhNsQ-NdTw9Ag",
    "Bri4bDh0xJFDiFMXnQ4QWA",
    "w27iN3KEPk1SYC63PauyTg",
    "ydISoORz5qxcVst0rf-ZjQ",
    "uTPu2KhLZ1b1GtkhIs7WSw",
    "MdNGMrvmjgVWvu2w5u7XPw",
    "OL2RHr5cqeFcezYpI4rQGA",
    "JtEwHTXY5dVvqw2zw3jkYQ"
]


def add_reviews_to_csv(new_reviews, csv_fil):
    fieldnames = ['text', 'rating']

    with open(csv_fil, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # If the file is empty, write headers
        if file.tell() == 0:
            writer.writeheader()

        for review in new_reviews['reviews']:
            print(review['text'])
            print(review['rating'])
            writer.writerow({
                'text': review['text'],
                'rating': review['rating']
            })


for business in business_ids:
    url = "https://api.yelp.com/v3/businesses/" + business + "/reviews?limit=50&sort_by=yelp_sort&page=25"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer 8aFMnycTG5WjzJ3hNlN6l_5vngRpSVRTf6rUPQwSGKlKxRKJhmq3EjdK6gZVADoVAS"
                         "-7I6dkTQy7mA6vsLokW-1J-o05YhjMN-0Jjt06YBipO5OFuPA3r7siuBjuZXYx"
    }
    response = requests.get(url, headers=headers)
    reviews = response.json()

    csv_file = 'reviews.csv'
    fieldnames = ['text', 'rating']
    add_reviews_to_csv(reviews, csv_file)
