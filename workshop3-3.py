
latency = 0
while latency < 120 or latency == "stop" :
    latency = int(input(f"what's the network latency :"))
    if latency == "stop":
        latency = str(latency)
        break 
    if latency >= 100:
        for _ in range(0,3):
            correction = input(f"Warning ! the latency is below 100 ms. did you correct it ? yes or no")

            if correction == "yes":
                print("it s back to normal")
                break
   
        if correction == "no":
            print("we have a MAJOR issue")
            break
            
           