#!/usr/bin/python3
"""using JSONPlaceholder REST API to get information about an employees
TODO and export them usin a csv format
"""

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    uri = f'https://jsonplaceholder.typicode.com/users/{argv[1]}/'

    u_data = requests.get(uri).json()
    td_data = requests.get(uri + 'todos')
    with open(f'{argv[1]}.csv', 'w') as csvFile:
        writter = csv.writer(csvFile, quotechar='"', quoting=csv.QUOTE_ALL)
        for i in td_data.json():
            writter.writerow(
                [i.get('userId'), u_data.get('username'), i.get('completed'),
                 i.get('title')]
                )
