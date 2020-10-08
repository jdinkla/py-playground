
import json

with open('data/example.json') as infile:
    data = json.load(infile)
    print(data)
    print(data["c"]["a"])
