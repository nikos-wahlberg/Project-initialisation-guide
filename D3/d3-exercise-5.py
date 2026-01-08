import requests
import json


response = requests.get('https://api.github.com/search/repositories?q=language:python')
data = response.json()

projects = data['items']

for project in projects:
    name = project['name']
    description = project['description']
    forks_count = project['forks_count']

    print(f"Name: {name}\nDescription: {description}\nForks: {forks_count}")