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
        user_list = []
        for td in td_data.json():
            if ud.get('id') == td.get('userId'):
                td_task = {}
                td_task['task'] = td.get('title')
                td_task['completed'] = td.get('completed')
                td_task['username'] = ud.get('username')
                user_list.append(td_task)
        dictFormat[ud.get('id')] = user_list

    with open('todo_all_employees.json', 'w') as jsonFile:
        dump(dictFormat, jsonFile)
