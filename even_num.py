#Create a list of numbers, print each number in the list that is even.

num = [1, 2, 3]

for number in num:
    if (number % 2) == 0:
        print(f"{number} is an even num")
    if (number % 2) != 0:
        print(f"{number} is an odd number")

