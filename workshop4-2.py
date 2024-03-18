server_tuple = ("name", "ip", "server_type", "state")
list_servers = []
 
while True:
    server_information = input("would you like to add a new server in inventory ? yes or no :")
    if server_information != "yes":
        break
    
    servers = []
    
    for server in server_tuple:
        
        info = input(f"enter this information, {server} : ")
        servers.append(info)
        
    servers = tuple(servers)
    list_servers.append(servers)
    print(servers)

for server in list_servers:
    (name, ip, type, state) = server
    print(f"name: {name}, ip: {ip} , type: {type} , state: {state} . ")    
print(list_servers)
        
