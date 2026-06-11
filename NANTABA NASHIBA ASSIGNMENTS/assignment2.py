# NANTABA NASHIBA
# 24/U/09665/PS

users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "customer": {"password": "cust123", "role": "Customer"},
    "cashier": {"password": "cash123", "role": "Cashier"}
}

coupon_discounts = {
    "SAVE10": 0.10,
    "SAVE20": 0.20,
    "NONE": 0.0
}

tax_rates = {
    "local": 0.05,
    "state": 0.08,
    "national": 0.12
}


def calculate_final_price(subtotal, coupon_code, location):
    coupon_code = coupon_code.upper()
    is_valid_coupon = coupon_code in coupon_discounts
    discount_rate = 0.0

    if is_valid_coupon:
        discount_rate = coupon_discounts[coupon_code]
        if coupon_code == "SAVE20":
            if subtotal >= 500:
                discount_rate = 0.25
            else:
                discount_rate = 0.20
        elif coupon_code == "SAVE10":
            if subtotal >= 200:
                discount_rate = 0.15
            else:
                discount_rate = 0.10
    else:
        discount_rate = 0.0

    if location.lower() in tax_rates:
        tax_rate = tax_rates[location.lower()]
        location_valid = True
    else:
        tax_rate = 0.10
        location_valid = False

    discount_amount = subtotal * discount_rate
    subtotal_after_discount = subtotal - discount_amount
    tax_amount = subtotal_after_discount * tax_rate
    final_price = subtotal_after_discount + tax_amount

    return {
        "subtotal": subtotal,
        "discount_rate": discount_rate,
        "discount_amount": discount_amount,
        "tax_rate": tax_rate,
        "tax_amount": tax_amount,
        "final_price": final_price,
        "coupon_code": coupon_code,
        "is_valid_coupon": is_valid_coupon,
        "location_valid": location_valid
    }


def print_price_details(details):
    print("\n--- Price Breakdown ---")
    print(f"Subtotal: USh {details['subtotal']:.2f}")
    if details['is_valid_coupon']:
        print(f"Coupon code: {details['coupon_code']}")
    else:
        print(f"Coupon code: {details['coupon_code']} (invalid, no discount)")
    print(f"Discount Rate: {details['discount_rate'] * 100:.0f}%")
    print(f"Discount Amount: USh {details['discount_amount']:.2f}")
    if details['location_valid']:
        print(f"Tax Rate: {details['tax_rate'] * 100:.0f}%")
    else:
        print(f"Tax Rate: {details['tax_rate'] * 100:.0f}% (default rate used)")
    print(f"Tax Amount: USh {details['tax_amount']:.2f}")
    print(f"Final Price: USh {details['final_price']:.2f}")
    print("------------------------\n")


def perform_purchase():
    try:
        subtotal = float(input("Enter product subtotal: USh "))
    except ValueError:
        print("Invalid subtotal. Please enter a number.")
        return

    if subtotal <= 0:
        print("Subtotal must be greater than zero.")
        return

    coupon_code = input("Enter coupon code (SAVE10, SAVE20, NONE): ").strip()
    location = input("Enter location (local, state, national): ").strip()

    result = calculate_final_price(subtotal, coupon_code, location)
    print_price_details(result)


def admin_menu():
    while True:
        print("\nAdmin options:")
        print("1. Calculate price")
        print("2. Show users")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            perform_purchase()
        elif choice == "2":
            print("\nRegistered users:")
            for name, data in users.items():
                print(f"- {name}: {data['role']}")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")


def customer_menu():
    print("\nCustomer access granted.")
    perform_purchase()


def cashier_menu():
    print("\nCashier access granted.")
    perform_purchase()


def main():
    print("Welcome to the simple E-commerce system")
    username = input("Username: ").strip().lower()
    password = input("Password: ").strip()

    if username in users and users[username]["password"] == password:
        role = users[username]["role"]
        print(f"\nLogin successful. Role: {role}")

        if role == "Admin":
            admin_menu()
        elif role == "Customer":
            customer_menu()
        elif role == "Cashier":
            cashier_menu()
    else:
        print("Invalid username or password.")


if __name__ == "__main__":
    main()
