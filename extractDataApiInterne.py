import requests                             #get the API
from requests.auth import HTTPBasicAuth     #manage basicAuth
import json                                 #manage JSON
import os                                   #manage Path and file
import getpass                              #hide password

from constants import USER

# URL API, must be interne.ovh.net and not pcc.eu.ovhcloud.tools
#ex: https://interne.ovh.net/uservice/gateway/pcc/v1/objects/datacenter?pccZone%3Aeq=rbx2a
print("(must be https://interne.ovh.net/uservice/gateway/pcc/v1 and not pcc.eu.ovhcloud.tools)")
url  = input("type the API Url:\n ")

user = USER

key_name = (f"{user}.key")
key_dir = "key"
key_file_path = os.path.join(key_dir, key_name)

if not os.path.exists(key_file_path):
    print(f"folder or file {key_file_path} doesnt exist, we will generate it")
    password = getpass.getpass("type your Jabber password: ")
    
    from secureConfig import encrypt_secure_config
    encrypt_secure_config(user=user, password=password)
    print("The key is generated")
    
else:
    with open(key_file_path , "rb") as key_file:
        key = key_file.read()

    from secureConfig import load_config, decrypt_data
    password_encrypted = load_config(filename='config.json', key='password_encrypted')
    password = decrypt_data(encrypted_data=password_encrypted, key=key)    

#Request the API    
reponse = requests.get(url, auth=HTTPBasicAuth(user, password))

if reponse.status_code == 200:
    donnees = reponse.json()

    file_dir  = "files"
    file_name = "data_api.json"
    file_path = os.path.join(file_dir, file_name)
    with open(file_path, 'w') as fichier:
        json.dump(donnees, fichier, indent=4)
        print(f"Data saved in {file_name}.")
    
else:
    print("Echec with code issue:", reponse.status_code)