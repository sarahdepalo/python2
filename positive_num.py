# Create a list of numbers, print each number in the list that is greater than zero

simple_list = [-1, -2, -3, 1, 2, 3]
positive_nums = []

for num in simple_list:
    if num > 0:
        positive_nums.append(num)

print(positive_nums)

