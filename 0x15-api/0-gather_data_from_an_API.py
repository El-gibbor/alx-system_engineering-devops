#!/usr/bin/python3
"""using JSONPlaceholder REST API to get information about an employees
TODO list progress with his/her employee ID
"""
import requests
from sys import argv

uri = f'https://jsonplaceholder.typicode.com/users/{argv[1]}/'
empl_data = requests.get(uri)
td_data = requests.get(uri + 'todos')

td_completed = [td for td in td_data.json() if td.get('completed') is True]

dn = len(td_completed)
td = len(td_data.json())

print(f"Employee {empl_data.json().get('name')} is done with tasks {dn}/{td}:")
for i in td_data.json():
    print(f"\t {i.get('title')}")
