from cryptography.fernet import Fernet
import json
import os

# Créer un dossier nommé "key" s'il n'existe pas déjà
key_dir = "key"
if not os.path.exists(key_dir):
    os.makedirs(key_dir)

# Chiffrer les informations sensibles
application_key = "52e7817f34346e67"
application_secret = "2b7fdb91405cc0a947c3bcbfd8e214ac"
consumer_key = "d52a2e371a5431baaa8f864061f42f1e"

# Générer une clé de chiffrement
key = Fernet.generate_key()

key_name = (f"{application_key}.key")

# Sauvegarder la clé dans un fichier
key_file_path = os.path.join(key_dir, key_name)
with open(key_file_path, "wb") as key_file:
    key_file.write(key)

# Créer un dictionnaire pour stocker les informations sensibles
sensitive_info = {
    "application_key": application_key,
    "application_secret": application_secret,
    "consumer_key": consumer_key
}

# Convertir le dictionnaire en format JSON
json_data = json.dumps(sensitive_info)

# Charger la clé de chiffrement
with open(key_file_path, "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)
encrypted_sensitive_info = {}
for key, value in sensitive_info.items():
    encrypted_value = cipher_suite.encrypt(value.encode()).decode()
    encrypted_sensitive_info[key + "_encrypted"] = encrypted_value

# Sauvegarder les données chiffrées dans un fichier JSON
encrypted_info = {"encrypted_data": encrypted_sensitive_info}
config_file_path = "config.json"
with open(config_file_path, "w") as config_file:
    json.dump(encrypted_info, config_file)
