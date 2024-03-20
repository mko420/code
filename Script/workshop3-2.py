storage = ["a","b","c"]
test_nok= 0
for i in storage:    
    test = int(input(f"what's the test result of the servers {i} :"))
    if test == 0:
        for _ in range(0,2):    
            test = int(input(f"what's the test result of the servers {i} :"))
            if test == 1:
                break
        if test == 0:
            test_nok += 1    
  
print(f" {test_nok} need a manual inspection.")