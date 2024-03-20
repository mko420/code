incident_priority = input("saisir un niveau de gravité pour un incident (par exemple, faible, modéré, élevé).")
match incident_priority:
    case "faible":
        print(f"the incident priority is {incident_priority}")
    case "modéré":
        print(f"the incident priority is {incident_priority}")
    case "élevé":
        print(f"the incident priority is {incident_priority}")