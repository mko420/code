utilisateurs = {}

def ajouter_utilisateur(user, role):
     utilisateurs[user] = role
    
    
def changer_role(user,role):

    if user not in utilisateurs.keys():
        return print(f"{user} not in list, what role is needed")     
    else:
        utilisateurs[user] = role
        return print(f"{user} has this role  ")
        
def afficher_utilisateurs():
    print(utilisateurs)        
                            
while True:
    print("1 - add a new user")
    print("2 - change the Role")
    print("3 - show the users")
    print("0 - quit the program")
    choice = int(input("Select a choice : " ))
    if choice == 3:
        afficher_utilisateurs()
    elif choice == 1:
        user = input(f"quel utilisateurs voulez vous ajouter ? ")
        role = input(f"quel role voulez vous ? ")
        ajouter_utilisateur(user, role)
    elif choice == 2:
        user = input(f"quel utilisateurs voulez vous modifier ? ")
        role = input(f"quel role voulez vous ? ")
        changer_role(user, role)
    elif choice == 0:
        print(f"exit the program ")
        break
    else:
        print("wrong choice")
        pass

    
    
    
    
