ressources_availables = input("le nombre total de ressources disponibles: ")
ressources_needed     = input("le nombre deressources demandées par un processus ")

ressources_allocated  = ressources_needed if ressources_needed < ressources_availables else 0

if ressources_allocated ==0:
    print("no ressources available")
else:
    print(f" the ressource is {ressources_allocated}")