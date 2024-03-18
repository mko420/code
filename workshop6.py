

bptotal = float(input("entrer la bande passante totale disponible dans le datacenter (en Gbps) : "))


    
priority_web = int(input("d'entrer la priorité du service WEB (sur une échelle de 1 à 3, 1 étant le plus haut). "))
#email = int(input("d'entrer la priorité du service EMAIL (sur une échelle de 1 à 3, 1 étant le plus haut). "))
#db = int(input("d'entrer la priorité du service DB (sur une échelle de 1 à 3, 1 étant le plus haut). "))

bp_web = float(input("'entrer demande de bande passante pour web (en Gbps). "))
#bp_email = input("'entrer demande de bande passante pour email (en Gbps). ")
#bp_web = input("'entrer demande de bande passante pour db (en Gbps). ")
bp_selected = bp_web if bp_web <= bptotal else (bptotal)
match priority_web:
    case 1:
        bp_web = bp_selected
    case 2:
        bp_web = bp_selected / 2
    case 3:
        bp_web = bp_selected / 3
    case _:
        bp_web = 0

        
print(f"la bande passante de web est {bp_web}")
    
    





