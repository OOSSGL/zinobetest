import sqlite3
import time
import pandas as pd

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
        start_time = time.time()
        country = {'region': region}

        country_and_language = get_country_and_language(region)
        country['name'] = country_and_language['name']
        country['language'] = country_and_language['language']

        # Hash language
        country['language'] = hash_language(country['language'])

        country['time'] = time.time() - start_time
        countries.append(country)

    # Create DataFrame
    df = pd.DataFrame(countries)

    print(df)

    df_times = df.agg({'time': ['sum', 'mean', 'min', 'max']})
    print(df_times)


