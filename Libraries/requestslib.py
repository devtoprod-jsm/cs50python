#pip install requests
import requests
import sys
import json
import importer

if len(sys.argv) != 2:
    sys.exit("Missing argument")
#https://itunes.apple.com/search?entity=song&limit=1&term=weezer

response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=50&term={sys.argv[1]}")

#print(response)
print(json.dumps(response.json(),indent=2))

for i in response.json()["results"]:
    print(i["trackName"])

importer.hello("Jai")
print(help(importer.hello))