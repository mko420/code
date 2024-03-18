logs =  ["ERROR: Échec de connexion", "INFO: Maintenance prévue à 23h00"]
priorite = "ERROR"
log_filtree = []
log_comptee = {}

def filtrer_logs(priorite):
    for log in logs:

        if priorite in log:
  
            log_filtree.append(log)

def compter_logs():
    priorite_log = set("ERROR", "INFO", "WARNING")
    for x in priorite_log:    
        for log in logs:
            if x in log:
                log_comptee.append...
            
      
filtrer_logs(priorite) 
print(log_filtree)   
    
