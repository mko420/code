#https://help.ovhcloud.com/csm/fr-ca-api-getting-started-ovhcloud-api?id=kb_article_view&sysparm_article=KB0042783

import json
import ovh
from cryptography.fernet import Fernet
import os

#variable to update
application_key = "52e7817f34346e67"

# Fonction pour charger la configuration depuis le fichier JSON
def load_config(filename, key):
    with open(filename, 'r') as f:
        data = json.load(f)
        encrypted_value = data["encrypted_data"][key]
        return encrypted_value

# Fonction pour déchiffrer les données
def decrypt_data(encrypted_data, key):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data.encode()).decode()
    return decrypted_data

key_name = (f"{application_key}.key")
key_dir = "key"
key_file_path = os.path.join(key_dir, key_name)

# check if folder/file exist
if not os.path.exists(key_file_path):
    print (f"folder or file {key_file_path} doesnt exist")

# Charger la clé de chiffrement
with open(key_file_path , "rb") as key_file:
    key = key_file.read()

# Charger les informations sensibles
application_key_encrypted = load_config('config.json', 'application_key_encrypted')
application_secret_encrypted = load_config('config.json', 'application_secret_encrypted')
consumer_key_encrypted = load_config('config.json', 'consumer_key_encrypted')

# Déchiffrer les informations sensibles
application_key = decrypt_data(application_key_encrypted, key)
application_secret = decrypt_data(application_secret_encrypted, key)
consumer_key = decrypt_data(consumer_key_encrypted, key)

client = ovh.Client(
    endpoint='ovh-ca',  # Changez si nécessaire
    application_key=application_key,
    application_secret=application_secret,
    consumer_key=consumer_key
)

pccname = client.get('/dedicatedCloud', 
    iamTags=None,
)
commercial_ranges = client.get('/dedicatedCloud/commercialRange')

for commercial_range_id in commercial_ranges:
    commercial_range_info = client.get(f'/dedicatedCloud/commercialRange/{commercial_range_id}')
    print("Informations sur le commercialRange :", commercial_range_info)
    print(json.dumps(commercial_range_info, indent=4))
