#List Operations

# Original list
my_list = ["apple", "orange", "cherry"]

# Add 1 new item
my_list.append("strawberry")

# Remove 1 item
my_list.remove("orange")

# Sort the list
my_list.sort()

print("Updated List:", my_list)


#Tuple Operations

# Original tuple
my_tuple = ("apple", "banana", "cherry")

# Try modifying one element
my_tuple[0] = "orange"


#Set Operations

# Original set
my_set = {"apple", "orange", "cherry"}

# Add a value
my_set.add("grapes")

# Remove a value
my_set.remove("orange")

# Print updated set
print("Updated Set:", my_set)


#Dictionary Operations

# Original dictionary
my_dict = {
    "name": "Marjorie",
    "age": 17
}

# Add a new key "grade"
my_dict["section"] = "1V"

# Update "age"
my_dict["age"] = 18

# Print all keys
print("Keys:", my_dict.keys())
