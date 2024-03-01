import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Iterate over a copy of the list to safely modify the original list
for number in random_numbers.copy():
    if number > 50:
        # Remove the number if it's greater than 50
        random_numbers.remove(number)
    else:
        # Find the index of the number and replace it with "XX"
        index = random_numbers.index(number)
        random_numbers[index] = "XX"

# Print the final list
print(random_numbers)
