import requests
import json
import hashlib


def get_regions():
    # Call service get all countries because there is no service to get all regions
    url = "https://restcountries-v1.p.rapidapi.com/all"

    headers = {
        'x-rapidapi-key': "b51660c4f3msh5e4bfd74ad56831p1514d4jsn5c8f09a6153f",
        'x-rapidapi-host': "restcountries-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    countries = json.loads(response.text)
    regions = {}

    # Get all regions
    for country in countries:
        regions[country['region']] = country['region']

    # Convert dict to list
    regions_list = list(regions.keys())
    # Remove last value because is "" empty
    regions_list.pop(-1)

    return regions_list


def get_country_and_language(region):
    # Call service to get countries of a region
    url = "https://restcountries.eu/rest/v2/region/{}".format(region)

    response = requests.request("GET", url)

    countries = json.loads(response.text)
    # Get name and first language of the first country of the region
    country = {
        'name': countries[0]['name'],
        'language': countries[0]['languages'][0]['name']
    }

    return country


def hash_language(language):
    m = hashlib.sha1()
    m.update(language.encode('utf-8'))

    return m.hexdigest()


def table_to_json(table, cur):
    cur.execute('Select * from {}'.format(table))
    # Python magic to convert sql result to json
    data_json = [dict((cur.description[i][0], value) for i, value in enumerate(row))
                 for row in cur.fetchall()]
    return data_json


def json_to_file(file_name, data):
    with open('{}.json'.format(file_name), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
