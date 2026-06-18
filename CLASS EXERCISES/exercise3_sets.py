# Exercise3 (Sets)

# 1. Use the set() constructor to create a set of 3 favorite beverages
beverages = set(["Coffee", "Tea", "Juice"])
print("Beverages set:", beverages)

# 2. Add 2 more items to the beverages set
beverages.add("Water")
beverages.add("Soda")
print("Beverages after adding 2 items:", beverages)

# 3. Check if microwave is present in the set
mySet = {"oven", "kettle", "microwave", "refrigerator"}
is_present = "microwave" in mySet
print("Is 'microwave' in the set?:", is_present)

# 4. Remove "kettle" from the set
mySet.remove("kettle")
print("Set after removing 'kettle':", mySet)

# 5. Loop through the set
print("Loop through the set:")
for item in mySet:
    print("  -", item)

# 6. Write a set of 4 items and a list of two items, add list elements to set elements
kitchen_items = {"pan", "pot", "spoon", "fork"}
new_items = ["knife", "plate"]
for item in new_items:
    kitchen_items.add(item)
print("Set after adding list items:", kitchen_items)

# 7. Two sets - one containing ages and one containing first names, then join them
ages_set = {18, 25, 30, 35}
names_set = {"Alice", "Bob", "Charlie", "Diana"}
joined_sets = ages_set.union(names_set)
print("Joined sets (ages and names):", joined_sets)
