
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = int(input("Enter your birth year: "))
city = input("Enter your city: ")

current_year = 2026
age = current_year - birth_year

print("\n--- Introduction ---")
print(f"My name is {first_name} {last_name}.")
print(f"I am {age} years old.")
print(f"I live in {city}.")