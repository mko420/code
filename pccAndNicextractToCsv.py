import requests                             #get the API
from requests.auth import HTTPBasicAuth     #manage basicAuth
import os                                   #manage Path and file
import getpass                              #hide password
import csv

from lib.constants import USER

url1      = "https://interne.ovh.net/uservice/gateway/pcc/v1/objects/datacenter?pccZone%3Aeq=eri1c"
url2_base = "https://interne.ovh.net/uservice/gateway/pcc/v1/objects/tools/microservice/getServiceNicsInfo"

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
response1 = requests.get(url1, auth=HTTPBasicAuth(user, password))

if response1.status_code == 200:
    list_pcc = response1.json()
    merged_data = []

    for pccItem in list_pcc:
        name = pccItem['name'].split('_')[0]  # Remove _XXXXX part
        url2 = f"{url2_base}?serviceName={name}"
        
        response2 = requests.get(url2, auth=HTTPBasicAuth(user, password))
        
        if response2.status_code == 200:
            pcc_serviceNics = response2.json()
            if pcc_serviceNics:
                data_column1 = pccItem['pccId']
                data_column2 = pccItem['pccZone']
                data_column3 = pccItem['state']
                data_column4 = pcc_serviceNics['nicTech']['nic']

                
                merged_data.append({'name': name,
                                    'pccId': data_column1,
                                    'pccZone': data_column2,
                                    'state': data_column3,
                                    'nicTech': data_column4})

    file_dir = "files"
    file_name = "merged_data.csv"
    file_path = os.path.join(file_dir, file_name)

    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['name', 'pccId', 'pccZone', 'state', 'nicTech']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for data_row in merged_data:
            writer.writerow(data_row)


    print(f"Merged data saved in {file_name}.")   
    
else:
    print("Echec with code issue:", response1.status_code)