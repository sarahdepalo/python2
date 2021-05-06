harry_potter_char = []
harry_potter_char.append("Harry Potter")
harry_potter_char.append("Ron")
harry_potter_char.append("Hermione")
harry_potter_char.append("Luna")
harry_potter_char.append("Neville")

# print(harry_potter_char[2])

index = 0

print(len(harry_potter_char))

#Here is a while loop! Yay! 
#It has a start at index and finishes at the end of the list
while index < len(harry_potter_char):
    print(harry_potter_char[index])
    index += 1

#Here is a FOR loop! Yay!
#For every item which is now called 'character' in harry_potter_char, print that single item's value
for character in harry_potter_char:
    print(character)


