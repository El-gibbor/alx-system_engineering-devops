#!/usr/bin/python3
"""using JSONPlaceholder REST API to get information about an employees
TODO list progress and export the data to json format
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    from json import dump

    uri = f'https://jsonplaceholder.typicode.com/users/{argv[1]}/'
    u_data = requests.get(uri).json()
    td_data = requests.get(uri + 'todos')

    td_list = []
    td_task = {}

    for td in td_data.json():
        td_task['task'] = td.get('title')
        td_task['completed'] = td.get('completed')
        td_task['username'] = u_data.get('username')
        td_list.append(td_task)

    jsonFormat = {u_data.get('id'): td_list}

    with open(f'{argv[1]}.json', 'w') as jsonFile:
        dump(jsonFormat, jsonFile)
