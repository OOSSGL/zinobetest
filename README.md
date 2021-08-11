# Zinobe test
To use the app first install the requirements
- pip install -r requirements.txt

Then you can run the app
- python app.py

It will do all the steps:

1. From https://rapidapi.com/apilayernet/api/rest-countries-v1, get all regions, done manually from getting all countries because there is no service to get all the regions.
2. From https://restcountries.eu/ get a country per region from point 1, it gets the first country.
3. From https://restcountries.eu/ also gets the name and the first language of the country, the language is hashed with SHA1
4. Creates the column Time were stores automatically the time spend in creating each row
5. With the PANDAS library creates a DataFrame table given the data
6. Using PANDAS library shows the total, mean, maximum and minimum time of the times of the table
7. Saves the tables to sqlite, the tables are Countries and Times, you can read then by executing sqlite3.exe
8. Creates a Json from each table and saves it in a file, the files are data.json and data_times.json

To run the test use the command pytest
- pytest

No framework was used in this project

Hours spend: 10

Made by Oscar David Garcia Medina