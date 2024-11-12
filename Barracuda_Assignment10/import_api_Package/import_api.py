# import_api.py

import requests
import json

def gpoAPI():
    response = requests.get("https://digimon-api.vercel.app/api/digimon/")
    json_string = response.content
    
    parsed_json = json.loads(json_string) # Now we have a python dictionary
    #print(parsed_json)

    for name in parsed_json["data"]:
        print(name)
gpoAPI()