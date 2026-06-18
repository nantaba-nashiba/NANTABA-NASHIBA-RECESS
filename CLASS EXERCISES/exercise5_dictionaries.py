# Exercise5 (Dictionaries)

# 1. Print the value of the shoe size
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print("Shoe size:", Shoes["size"])

# 2. Change the value "Nick" to "Adidas"
Shoes["brand"] = "Adidas"
print("Shoes after changing brand:", Shoes)

# 3. Add a key/value pair "type": "sneakers" to the dictionary
Shoes["type"] = "sneakers"
print("Shoes after adding type:", Shoes)

# 4. Return a list of all the keys in the dictionary
keys_list = list(Shoes.keys())
print("All keys:", keys_list)

# 5. Return a list of all the values in the dictionary
values_list = list(Shoes.values())
print("All values:", values_list)

# 6. Check if the key "size" exists in the dictionary
key_exists = "size" in Shoes
print("Does 'size' key exist?:", key_exists)

# 7. Loop through the dictionary
print("Loop through dictionary:")
for key, value in Shoes.items():
    print(f"  {key}: {value}")

# 8. Remove "color" from the dictionary
Shoes.pop("color")
print("Shoes after removing color:", Shoes)

# 9. Empty the dictionary
Shoes.clear()
print("Shoes after clearing:", Shoes)

# 10. Create a dictionary of your choice and make a copy of it
student = {
    "name": "John",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Science", "English"]
}
student_copy = student.copy()
print("Original student dict:", student)
print("Copied student dict:", student_copy)

# 11. Show nested dictionaries
employees = {
    "employee1": {
        "name": "Alice",
        "position": "Manager",
        "salary": 50000
    },
    "employee2": {
        "name": "Bob",
        "position": "Developer",
        "salary": 40000
    },
    "employee3": {
        "name": "Charlie",
        "position": "Designer",
        "salary": 35000
    }
}
print("Nested dictionaries (employees):")
for employee_id, employee_info in employees.items():
    print(f"  {employee_id}:")
    for key, value in employee_info.items():
        print(f"    {key}: {value}")
