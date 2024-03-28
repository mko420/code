#### LIB ####
from sqlalchemy import create_engine, text
import os
from lib.constants import *
from lib.tools import getCredentials_secure_data, getHost_commercial_range, extract_mysql_Csv

#### FUNCTIONS #####
def request_and_extract_data(dict_Credentials, zone):
    connection, query = getHost_commercial_range(
    user     = dict_Credentials["username"],
    password = dict_Credentials["password"],
    host     = dict_Credentials["ip_address"],
    port     = dict_Credentials["port"],
    database = dict_Credentials["database_name"],
    )

    file_path = f"{REPO_SDEV}/extract_Hosts_{zone}.csv"
    extract_mysql_Csv(data=query, file=file_path)

    print(f"Résultat de la requête SQL a été enregistré dans {file_path}")

    connection.close()

#### SCRIPT ####
#INPUT
data_wanted = input("do you want to connect to your private Database ? yes or no : ")

if data_wanted =="no":
    zone_wanted = input("What's zone do you want ? all for all zone or zone wanted ( ex: rbx2b): ")

#PRIVATE DB RBX2A
if data_wanted == "yes":    
    request_and_extract_data(dict_Credentials=INFORMATIONS_PRIVATEDB, zone=INFORMATIONS_PRIVATEDB["zone"])
        
# ALL ZONES
elif data_wanted == "no" and zone_wanted == "all":
    for zone in ALL_ZONES:
        informations = getCredentials_secure_data(zone=zone)
        request_and_extract_data(dict_Credentials=informations, zone=zone)

#SELECTED ZONE                   
elif data_wanted == "no" and zone_wanted != "all":
    informations = getCredentials_secure_data(zone=zone_wanted)
    request_and_extract_data(dict_Credentials=informations, zone=zone_wanted)