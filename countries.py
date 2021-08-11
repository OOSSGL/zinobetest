import requests


def get_regions():
    url = "https://restcountries-v1.p.rapidapi.com/all"

    headers = {
        'x-rapidapi-key': "b51660c4f3msh5e4bfd74ad56831p1514d4jsn5c8f09a6153f",
        'x-rapidapi-host': "restcountries-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)
