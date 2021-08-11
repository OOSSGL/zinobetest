import sqlite3
from countries import get_regions

# BD
con = sqlite3.connect('zinobe.db')

if __name__ == '__main__':
    print('Hi')
    get_regions()
