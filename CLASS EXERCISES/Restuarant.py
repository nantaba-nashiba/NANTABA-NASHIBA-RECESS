class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

    def set_number_served(self, number):
        if number >= 0:
            self.number_served = number
        else:
            print("Number served cannot be negative.")

    def increment_number_served(self, additional_customers):
        if additional_customers >= 0:
            self.number_served += additional_customers
        else:
            print("Cannot increment by a negative number.")


restaurant = Restaurant("Nana's Bistro", "Ugandan")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(10)
restaurant.increment_number_served(5)
print(f"Number of customers served: {restaurant.number_served}")
