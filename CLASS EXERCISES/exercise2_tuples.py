# Exercise2 (Tuples)

# 1. Consider the tuple - output your favorite phone brand
x = ("samsung", "iphone", "tecno", "redmi")
print("Favorite phone brand:", x[1])

# 2. Use negative indexing to print the 2nd last item in your tuple
print("2nd last item (negative indexing):", x[-2])

# 3. Update "iphone" to "itel" (tuples are immutable, so we create a new tuple)
x_updated = ("samsung", "itel", "tecno", "redmi")
print("Tuple after updating iphone to itel:", x_updated)

# 4. Add "Huawei" to your tuple (create a new tuple)
x_with_huawei = x_updated + ("Huawei",)
print("Tuple after adding Huawei:", x_with_huawei)

# 5. Loop through the tuple
print("Loop through phones:")
for phone in x:
    print("  -", phone)

# 6. Remove/delete the first item in your tuple (create a new tuple)
x_removed = x[1:]
print("Tuple after removing first item:", x_removed)

# 7. Using the tuple() constructor, create a tuple of the cities in Uganda
uganda_cities = tuple(["Kampala", "Gulu", "Mbarara", "Fort Portal", "Jinja"])
print("Uganda cities tuple:", uganda_cities)

# 8. Unpack your tuple
city1, city2, city3, city4, city5 = uganda_cities
print("Unpacked cities:")
print(f"  City 1: {city1}, City 2: {city2}, City 3: {city3}, City 4: {city4}, City 5: {city5}")

# 9. Use a range of indexes to print the 2nd, 3rd and 4th cities
print("Cities at index 1, 2, 3:", uganda_cities[1:4])

# 10. Two tuples - first names and second names, then join them
first_names_tuple = ("John", "Jane", "James")
second_names_tuple = ("Smith", "Doe", "Brown")
joined_tuples = first_names_tuple + second_names_tuple
print("Joined tuples:", joined_tuples)

# 11. Create a tuple of colors and multiply it by 3
colors = ("Red", "Blue", "Green")
colors_multiplied = colors * 3
print("Colors multiplied by 3:", colors_multiplied)

# 12. Return the number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print("Number of times 8 appears:", count_8)
