import sqlite3
from countries import get_regions, get_country_and_language, hash_language

# BD
con = sqlite3.connect('zinobe.db')

if __name__ == '__main__':
    # Get regions
    regions = get_regions()
    print(regions)

    # Get first country of each region
    countries = []
    for region in regions:
        country = get_country_and_language(region)
        countries.append(country)
    print(countries)

    # Hash languages
    for country in countries:
        country['language'] = hash_language(country['language'])

    print(countries)
