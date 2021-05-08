#Base catalog that holds all the original numbers
catalog = {
    "Igor" : "859-485-2935",
    "Jazz" : "334-584-2345",
    "Melissa": "584-394-5857",
    
}

program_end = True

while program_end == True:
    print("Electronic Phone Book \n")
    print("======================")
    print("\n 1. Look up an entry \n 2. Set an entry \n 3. Delete an entry \n 4. List all entries \n 5. Quit")
    user_input = int(input("What do you want to do? Pick a number from 1 - 5: "))
    #Look Up an Entry
    if (user_input == 1):
        name_selection = int(input("What name would you like to look up? Enter a number 1 -3: \n 1. Igor \n 2. Jazz \n 3. Melissa \n"))
        if (name_selection == 1):
            print(catalog["Igor"])
        elif name_selection == 2:
            print(catalog["Jazz"])
        elif name_selection == 3:
            print(catalog["Melissa"])
        else:
            print("Please type a number from 1 -3.")
   #Set an entry
    if (user_input == 2):
        user_name = input("Enter your name: ")
        user_number = input("Ener your phone number: ")
    #Delete an Entry:
    if(user_input == 3):
        print(catalog)
        entry_to_delete = input("Whose entry would you like to delete?  ")
        if entry_to_delete == "Melissa":
            del catalog["Melissa"]
            print("The entry for Melissa has been deleted.")
        elif entry_to_delete == "Igor":
            del catalog["Igor"]
            print("The entry for Igor has been deleted.")
        elif entry_to_delete == "Jazz":
            del catalog["Jazz"]
            print("The entry for Jazz has been deleted.")
        else:
            print("We don't have that name in our database.")
    # List all Entries
    if (user_input == 4):
        for name in catalog.items():
            print(name)
    # Quit the Program
    if (user_input == 5):
        print("See you next time!")
        program_end = False





