import requests                             #get the API
from requests.auth import HTTPBasicAuth     #manage basicAuth
import os                                   #manage Path and file
import getpass                              #hide password

from lib.constants import USER

# URL API, must be interne.ovh.net and not pcc.eu.ovhcloud.tools
#ex: https://interne.ovh.net/uservice/gateway/pcc/v1/objects/datacenter?pccZone%3Aeq=rbx2a
print("(must be https://interne.ovh.net/uservice/gateway/pcc/v1 and not pcc.eu.ovhcloud.tools)")
#url  = input("type the API Url:\n ")
url = "https://interne.ovh.net/uservice/gateway/pcc/v1/objects/datacenter?pccZone%3Aeq=rbx2a"

user = USER

key_name = (f"{user}.key")
key_dir = "key"
key_file_path = os.path.join(key_dir, key_name)

if not os.path.exists(key_file_path):
    print(f"folder or file {key_file_path} doesnt exist, we will generate it")
    password = getpass.getpass("type your Jabber password: ")
    
    from lib.secureConfig import encrypt_secure_config
    encrypt_secure_config(user=user, password=password)
    print("The key is generated")
    
else:
    with open(key_file_path , "rb") as key_file:
        key = key_file.read()

    from lib.secureConfig import load_config, decrypt_data
    password_encrypted = load_config(filename='config.json', key='password_encrypted')
    password = decrypt_data(encrypted_data=password_encrypted, key=key)    

#Request the API    
reponse = requests.get(url, auth=HTTPBasicAuth(user, password))

if reponse.status_code == 200:
    data = reponse.json()

    file_dir  = "files"
    file_name = "data_api.csv"
    file_path = os.path.join(file_dir, file_name)
    selected_columns = ['pccId', 'pccZone', 'name']
    
    from lib.tools import extract_to_csv
    extract_to_csv(file_path=file_path, data=data, columns=selected_columns)
    print(f"Data saved in {file_name}.")    
    
else:
    print("Echec with code issue:", reponse.status_code)