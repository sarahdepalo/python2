list_of_num = [4, 8, 12]
total = 0 #good starting place for math problems. Acts as a placeholder here. 

#Prints the new total each time: "The total is now..."
for num in list_of_num:
    total = total + num
    print("The total is now: " + str(total))

#This prints just the final sum:
#These can't both run at the same time!!
for num in list_of_num:
    total = total + num

print("The total is now " + str(total))