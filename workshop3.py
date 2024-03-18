servers = ["a","b","c"]
poweron = 0
poweroff= 0
for i in servers:    
    actif = int(input(f"what's the state of the servers {i} :"))
    if actif == 1:
        poweron +=  1
    else:
        poweroff += 1    
print(f" {poweron} servers are power on and {poweroff} are poweroff.")1