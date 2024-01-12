#!/usr/bin/python3
"""using JSONPlaceholder REST API get and user TODO list data
 to json in a dictionary of list of dictionaries format
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    from json import dump

    uri = f'https://jsonplaceholder.typicode.com/'
    u_data = requests.get(uri + 'users')
    td_data = requests.get(uri + 'todos')

    dictFormat = {}

    for ud in u_data.json():
        user_todoList = [
            {
                'username': td.get('username'),
                'task': td.get('title'),
                'completed': ud.get('completed')
            }
            for td in td_data.json() if ud.get('id') == td.get('userId')
        ]
        dictFormat[ud.get('id')] = user_todoList

    with open('todo_all_employees.json', 'w') as jsonFile:
        dump(dictFormat, jsonFile)
