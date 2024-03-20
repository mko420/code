services = {
    "web":{"name":"web"}, 
    "email":{"name":"email"}, 
    "db":{"name":"db"},
    }

#service_priority = services[service]["priority"]
#service_bandwidth = services[service]["bandwitdh"]
    
def calculate_bandwidth(bptotalavailable, service, bptotalneeded):
    
    service            = services[service]["name"]
    priority           = services[service]["priority"]
    bandwidth          = services[service]["bandwidth"]
    bandwidth_selected = bandwidth if bandwidth <= bptotalavailable else bptotalavailable
    nb_services        = len(services)
    
    if bptotalneeded > bptotalavailable:
        if priority == 1 and bandwidth_selected > (bptotalavailable*0.75):
            bandwidth = bandwidth_selected - ((bptotalneeded - bptotalavailable) / nb_services)
            return bandwidth
        elif priority == 2 and bandwidth_selected > ((bptotalavailable*0.5)*0.75):
            bandwidth = bandwidth_selected - ((bptotalneeded - bptotalavailable) / nb_services)
            return bandwidth          
        elif priority == 3 and bandwidth_selected > ((bptotalavailable*0.5)*0.25):
            bandwidth = bandwidth_selected - ((bptotalneeded - bptotalavailable) / nb_services)
            return bandwidth
        else:
            return bandwidth 
    else:
        return bandwidth_selected

def calculated(services,total_bandwidth_needed_calculated):
    total_bandwidth_needed_calculated = 0.00
    for service in services:
        print(service)
        services[service]["bandwidth"] = calculate_bandwidth(bptotalavailable=total_bandwidth_available,service=service, bptotalneeded=total_bandwidth_needed)
        print(services[service]["bandwidth"])
        total_bandwidth_needed_calculated += services[service]["bandwidth"]    
        print(total_bandwidth_needed_calculated)
         
total_bandwidth_needed    = 0
total_bandwidth_available = float(input("entrer la bande passante totale disponible dans le datacenter (en Gbps) : "))

for service in services:
    service_name = services[service]["name"]
    services[service]["priority"]  = int(input(f"entrer la priorité du service {service_name} (sur une échelle de 1 à 3, 1 étant le plus haut). "))    
    services[service]["bandwidth"] = float(input(f"entrer la demande de bande passante pour {service_name} : "))
    total_bandwidth_needed += services[service]["bandwidth"]


total_bandwidth_needed_calculated = 0.00
flag_bandwidth = True
while flag_bandwidth == True and total_bandwidth_needed_calculated < (total_bandwidth_available - 0.5):
    calculated(services, total_bandwidth_needed_calculated)
    if total_bandwidth_needed_calculated + total_bandwidth_available >= (total_bandwidth_available-0.5):
        calculated(services, total_bandwidth_needed_calculated)
        flag_bandwidth = False

print(total_bandwidth_needed_calculated)
print(services)