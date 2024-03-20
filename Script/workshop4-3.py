inventory = {
    "serveurs" : 0,
    "routeurs" : 0,
    "switch" : 0,    
}

while inventory:
    user_choice = input(f"voulez vous ajouter ou retirer une unité ou stopper (fin) : ")
    if user_choice == "fin":
        break
    user_type   = input(f" quel type voulez vous mettre a jour : (serveurs, routeurs, switch) ")
    user_number = int(input(f" Combien d unité voulez vous {user_choice} : "))

    if user_choice == "ajouter":
        inventory[user_type] += user_number
    elif user_choice == "retirer":
            if inventory[user_type] == 0:
                pass
            else:
                inventory[user_type] -= user_number
    print(inventory)

print(inventory)    
    
