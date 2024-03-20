maintenance_list = []
flag_task = False
while flag_task == False:
    maintenance=input("add the maintenance task for the day : (stop to finish the setup)")
    if maintenance == "stop":
        flag_task = True
    else:
        maintenance_list.append(maintenance)
        
print (maintenance_list)
    
while maintenance_list:
    for maintenance in maintenance_list:
        x = input(f"did you do this task {maintenance} : yes or no ")
        maintenance_index = maintenance_list.index(maintenance)
        if x == "yes":
            maintenance_list.pop(maintenance_index)
    print(maintenance_list)
