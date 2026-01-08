"""import json
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

print(f"Reading from: {args.input}")"""


import json
import requests
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description="Fetch cat facts from an API")
parser.add_argument('--input', type=int, default=5, help='Number of cat facts to fetch')
args = parser.parse_args()

api_list = []
for i in range(args.input):
    response = requests.get('https://catfact.ninja/fact')
    api_list.append(response.json())

# --- NEW: Save to a file so you can check it later ---
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"cat_facts_{timestamp}.json"

with open(filename, "w") as f:
    json.dump(api_list, f, indent=2)

print(f"Success! Saved to {filename}")