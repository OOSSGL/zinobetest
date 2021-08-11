import sqlite3
import time
import json
import pandas as pd

from utilities import get_regions, get_country_and_language, hash_language, table_to_json, json_to_file

# BD
con = sqlite3.connect('zinobe.db')

if __name__ == '__main__':
    # Get regions
    regions = get_regions()

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

    # DataFrames to tables
    df.to_sql(name='Countries', con=con, if_exists='replace')
    df_times.to_sql(name='Times', con=con, if_exists='replace')

    # DB tables to json
    data_json = table_to_json('Countries', con.cursor())
    data_times_json = table_to_json('Times', con.cursor())

    con.close()

    # Json to file
    json_to_file('data', data_json)
    json_to_file('data_times', data_times_json)
