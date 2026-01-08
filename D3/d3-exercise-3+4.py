import json
import requests
import argparse

parser = argparse.ArgumentParser(description="Fetch cat facts from an API")
parser.add_argument('--input', type=int, default=5, help='Number of cat facts to fetch')

args = parser.parse_args()



api_list = []
for i in range(args.input):
    response = requests.get('https://catfact.ninja/fact')
    api_list.append(response.json())

for res in api_list:
    print(res["fact"])

print(f"Reading from: {args.input}")