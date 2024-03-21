from cryptography.fernet import Fernet
import json
import os

def encrypt_secure_config(**kwargs):
    
    if ('application_key' in kwargs and 'application_secret' in kwargs and 'consumer_key' in kwargs) or ('user' in kwargs and 'password' in kwargs):
    
        key_dir = "key"
        if not os.path.exists(key_dir):
            os.makedirs(key_dir)

        key = Fernet.generate_key()
        
        if 'application_key' in kwargs:    
            key_name = (f"{kwargs['application_key']}.key")
        else:
            key_name = (f"{kwargs['user']}.key")

        key_file_path = os.path.join(key_dir, key_name)
        with open(key_file_path, "wb") as key_file:
            key_file.write(key)

        sensitive_info= {}
        
        if 'application_key' in kwargs:
            sensitive_info = {
                "application_key": kwargs['application_key'],
                "application_secret": kwargs['application_secret'],
                "consumer_key": kwargs['consumer_key'],
            }
        else:
            sensitive_info = {
                "user": kwargs['user'],
                "password": kwargs['password'],
            }

        json_data = json.dumps(sensitive_info)

        with open(key_file_path, "rb") as key_file:
            key = key_file.read()

        cipher_suite = Fernet(key)
        encrypted_sensitive_info = {}
        for key, value in sensitive_info.items():
            encrypted_value = cipher_suite.encrypt(value.encode()).decode()
            encrypted_sensitive_info[key + "_encrypted"] = encrypted_value

        encrypted_info = {"encrypted_data": encrypted_sensitive_info}
        config_file_path = "config.json"
        with open(config_file_path, "w") as config_file:
            json.dump(encrypted_info, config_file)
    else:
        raise ValueError("Nombre d'arguments invalide.")


