# Exercise1 (Lists)

# 1. A list with 5 items (names of people) and output the 2nd item
people = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
print("2nd item:", people[1])

# 2. Change the value of the first item to a new value
people[0] = "Alexander"
print("List after changing first item:", people)

# 3. Add a sixth item to the list
people.append("Frank")
print("List after adding 6th item:", people)

# 4. Add "Bathel" as the 3rd item in the list
people.insert(2, "Bathel")
print("List after inserting Bathel at position 3:", people)

# 5. Remove the 4th item from the list
people.pop(3)
print("List after removing 4th item:", people)

# 6. Use negative indexing to print the last item in the list
print("Last item (negative indexing):", people[-1])

# 7. Create a new list with 7 items and print the 3rd, 4th and 5th items
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]
print("Items at index 2, 3, 4:", fruits[2:5])

# 8. Write a list of countries and make a copy of it
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda", "Burundi"]
countries_copy = countries.copy()
print("Original countries:", countries)
print("Copied countries:", countries_copy)

# 9. Loop through the list of countries
print("Countries loop:")
for country in countries:
    print("  -", country)

# 10. Write a list of animal names and sort them in ascending and descending order
animals = ["Zebra", "Elephant", "Lion", "Giraffe", "Antelope", "Bear"]
animals_asc = sorted(animals)
animals_desc = sorted(animals, reverse=True)
print("Animals (ascending):", animals_asc)
print("Animals (descending):", animals_desc)

# 11. Output only animal names with the letter 'a' in them
animals_with_a = [animal for animal in animals if 'a' in animal.lower()]
print("Animals with letter 'a':", animals_with_a)

# 12. Two lists - first names and second names, then join them
first_names = ["John", "Jane", "James"]
second_names = ["Smith", "Doe", "Brown"]
# Combine corresponding first and second names into full names
full_names = [f"{f} {s}" for f, s in zip(first_names, second_names)]
print("Joined lists:", full_names)
