#LISTS ARE MUTABLE

my_list = [1, 2, 3, 4]
print("Original List:", my_list)

# Modifying an element
my_list[2] = "Python"
print("Modified List:", my_list)

# Adding an element
my_list.append("New Element")
print("List after Adding an Element:", my_list)

#STRINGS ARE NOT

my_string = "Hello"
print("Original String:", my_string)

# Attempting to modify a character in the string
try:
    my_string[1] = "a"
except TypeError as e:
    print("Error:", e)

# Constructing a new string
new_string = "H" + "a" + my_string[2:]
print("Altered String:", new_string)
