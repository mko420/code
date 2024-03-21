import requests
from requests.auth import HTTPBasicAuth
import json
import os
from encryptKey import encrypt_secure_config

# URL API, must be interne.ovh.net and not the new DNS name
url = "https://interne.ovh.net/uservice/gateway/pcc/v1/objects/datacenter?pccZone%3Aeq=rbx2a"

user = 'michael.castaing'

key_name = (f"{user}.key")
key_dir = "key"
key_file_path = os.path.join(key_dir, key_name)

if not os.path.exists(key_file_path):
    print(f"folder or file {key_file_path} doesnt exist, we will generate it")
    password = input("type your Jabber password: ")
    encrypt_secure_config(user=user, password=password)
    print("The key is generated")
    
reponse = requests.get(url, auth=HTTPBasicAuth(user, password))

if reponse.status_code == 200:
    donnees = reponse.json()

    with open('donnees_api.json', 'w') as fichier:
        json.dump(donnees, fichier, indent=4)
        print("Data saved in 'donnees_api.json'.")
    
else:
    print("Echec with code issue:", reponse.status_code)