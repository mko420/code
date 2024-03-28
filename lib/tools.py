#extraction.py

import csv
import json
import requests
import getpass
import os
from sqlalchemy import create_engine, text

def extract_to_csv(file_path,data, columns=None):
    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        if columns == None: 
            csv_writer.writerow(data[0].keys())
            for row in data:
                csv_writer.writerow(row.values())
        else:
            csv_writer.writerow(columns)
            for row in data:
                csv_writer.writerow([row[column] for column in columns])

def extract_to_json(file_path,data):
        with open(file_path, 'w') as fichier:
            json.dump(data, fichier, indent=4)
            
def extract_mysql_Json(data, file):
    columns = data.keys()

    result_dict_list = [dict(zip(columns, row)) for row in data.fetchall()]

    with open(file, 'w') as output_file:
        return json.dump(result_dict_list, output_file, indent=4)
    
def extract_mysql_Csv(data, file):    
    with open(file, 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(data.keys())    
        csv_writer.writerows(data.fetchall())

def manageUservAuth(user=None, password=None, method='basic'):
    """get user/passwd and generate a HTTPBasicAuth object.
       if no user is provided, user AND password will be requested.
       if no password is provided, it will be requested.

    """
    if user is None:
        print("Need user name")
        user = input("Enter User name:")
        password = getpass()
    elif password is None:
        print("Need a password")
        password = getpass()
    if method == "digest":
        authObj = requests.auth.HTTPDigestAuth(user, password)
    else:
        authObj = requests.auth.HTTPBasicAuth(user, password)
    return authObj 

def getCredentials_secure_data(zone):        
    if zone == "rbx2a":
        database = "privateCloud"
    else:
        database = f"privateCloud_{zone}"
    
    from lib.constants import USER_LOGIN8
    file_path  = f'/home/{USER_LOGIN8}/wd/bootstrapdev/docker/generated/secure_datas/mozg/{zone}/secure_data.dev3'
    
    informations = {
        "database_name": database,
        "ip_address": None,
        "username": None,
        "password": None,
        "port": None
    }
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                parts = line.split('::')
                
                if parts[0] == database:
                    if len(parts) >= 5:
                        informations["database_name"] = parts[0]
                        informations["ip_address"] = parts[1]
                        informations["username"] = parts[2]
                        informations["password"] = parts[3]
                        informations["port"] = parts[4]

                        return informations
    else:
        print("Le fichier secure_data.dev3 n'existe pas or not in good format.")
    return informations

def getHost_commercial_range(user,password,host,port,database):
    connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(connection_string)
    connection = engine.connect()

    query = connection.execute(text('''
        SELECT 
            host.id AS hostId,
            host.hostName AS hostName,
            host.profile AS hostProfile,
            host.state AS hostState,
            hardware_profile.state AS serverState,
            host.serverProfile AS serverProfile,
            hardware_profile.cpu AS cpu,
            hardware_profile.ram AS ram,
            host.osId,
            host.datacenterId AS datacenterId,
            commercialRange.name AS datacenterCommercialRange,
            host.pccId AS pccId,
            host.billingType AS billingType
        FROM
            host
        INNER JOIN 
            hardware_profile ON host.hardwareProfileId = hardware_profile.id
        INNER JOIN 
            datacenter ON host.datacenterId = datacenter.id
        INNER JOIN 
            commercialRange ON datacenter.commercialRangeId = commercialRange.id
    '''))
    return (connection, query)