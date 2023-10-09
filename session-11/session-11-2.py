Details = {"Destination": [], "Nationality": [], "Age": []}

print("Original:", Details)

# appending the list
while True:
    
    Details["Destination"].append(input("Destination:"))
    Details["Nationality"].append(input("Nationality:"))
    Details["Age"].append(input("Age:"))
    
    cmd=input("Do you want to continue? (y/n)")
    
    if cmd.lower() in ["n", "no"]:
        break
   
   
#Details["Age"] += [20, 40, 50]
print("Modified:", Details)