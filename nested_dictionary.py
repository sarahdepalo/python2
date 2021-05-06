digitalCrafts = {
    "US" : {
        "Georgia" : {
            "Atlanta" : "3423 Piedmont Rd NE #420"
        },
        "Texas" : {
            "Houston" : "1334 Brittmore Rd"
        }
    }
}


#prints all the nested dictionaries
print(digitalCrafts)
print("---------------")
#Prints just the Georgia campus info:
print(digitalCrafts["US"]["Georgia"]["Atlanta"])