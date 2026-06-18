# Exercise4 (Strings)

# 1. Declare two variables, integer and string, and concatenate them
age = 25
name = "Alice"
concatenated = name + " is " + str(age) + " years old"
print("Concatenated string:", concatenated)

# 2. Output the string without spaces at the beginning, in the middle and at the end
txt = "      Hello,       Uganda!       "
cleaned_txt = txt.strip().replace("       ", " ")
print("String without extra spaces:", cleaned_txt)

# 3. Convert the value of 'txt' to uppercase
txt_upper = txt.upper()
print("Uppercase string:", txt_upper)

# 4. Replace character 'U' with 'V' in the string
txt_replaced = txt.replace("U", "V")
print("String with U replaced by V:", txt_replaced)

# 5. Return a range of characters in the 2nd, 3rd and 4th position
y = "I am proudly Ugandan"
substring = y[1:4]
print("Characters at positions 1, 2, 3:", substring)

# 6. Correct the error in this code
x = "All \"Data Scientists\" are cool!"
print("Corrected string:", x)
