meal = {
    "drink": "vodka soda",
    "entree": "spaghetti and meatballs",
    "dessert": "ice cream sandwich",
}

# print(meal["dessert"])

# print("Tonight I will have %s for dinner, with an %s for dessert. I'll have a %s as my drink" % (meal["entree"], meal["dessert"], meal["drink"]))

# # If the key "dessert" is found in the dictionary 'meal': 
# if "dessert" in meal:
#     print("OF COURSE Sarah had dessert!")
# else:
#     print("Sarah did NOT have dessert, and now she is sad.")

print(meal)
#Add a NEW key and value:
meal["appetizer"] = 'house salad'
#Update the key "drink" with the value "sweet tea"
meal["drink"]  = "sweet tea"
print(meal)
#Delete an entry by referencing its key:
del meal["dessert"]
print(meal)