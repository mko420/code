set_identifiant = set()

while True:
    identifiant = input(f"veuillez saisir votre identifiant:  ")
    if identifiant  not in set_identifiant:
        set_identifiant.add(identifiant)

    print(set_identifiant)

    
    
    
    
