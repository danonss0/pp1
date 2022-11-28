import json


film = {
    "tytul": "Samsung",
    "rezyser": "James Cameron",
    "rok": 2009,
    "aktorzy": ["Sam Worthington","Zoe Saldana","Sigourney Weaver"],
    "ocena": "10/10"
   }
print(film)

with open("sample.json", "w") as outfile:
    outfile.write(json.dumps(film, indent=4))