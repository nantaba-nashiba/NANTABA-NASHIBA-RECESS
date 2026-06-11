# NANTABA NASHIBA
# 24/U/09665/PS

def get_bill_amount():
    """Get and validate the total bill amount from the user."""
    while True:
        try:
            bill = float(input("Enter the total bill amount: $"))
            if bill < 0:
                print("Please enter a positive amount.")
                continue
            return bill
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_num_people():
    """Get and validate the number of people from the user."""
    while True:
        try:
            people = int(input("Enter the number of people: "))
            if people <= 0:
                print("Please enter a positive number.")
                continue
            return people
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def get_tip_percentage():
    """Get the tip percentage from the user with predefined options."""
    while True:
        print("\nTip Options:")
        print("1. 10%")
        print("2. 15%")
        print("3. 20%")
        print("4. Custom")
        
        choice = input("Select tip option (1-4): ")
        
        if choice == "1":
            return 10
        elif choice == "2":
            return 15
        elif choice == "3":
            return 20
        elif choice == "4":
            try:
                custom_tip = float(input("Enter custom tip percentage: "))
                if custom_tip < 0:
                    print("Please enter a positive percentage.")
                    continue
                return custom_tip
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
        else:
            print("Invalid choice. Please select 1-4.")

def main():
    """Main program flow."""
    print("=" * 50)
    print("BILL SPLIT CALCULATOR".center(50))
    print("=" * 50)
    
    # Gets user inputs with validation
    bill_amount = get_bill_amount()
    num_people = get_num_people()
    tip_percent = get_tip_percentage()
    
    # Calculates values
    tip_amount = bill_amount * (tip_percent / 100)
    total_bill = bill_amount + tip_amount
    per_person_share = total_bill / num_people
    
    # Displays receipt
    print("\n" + "=" * 50)
    print("RECEIPT".center(50))
    print("=" * 50)
    print(f"Subtotal:           ${bill_amount:>10.2f}")
    print(f"Tip ({tip_percent}%):          ${tip_amount:>10.2f}")
    print(f"Total Bill:         ${total_bill:>10.2f}")
    print("-" * 50)
    print(f"Number of People:   {num_people:>10}")
    print(f"Per Person Share:   ${per_person_share:>10.2f}")
    print("=" * 50)
    
    # Displays individual shares
    print(f"\nEach person should pay: ${per_person_share:.2f}")

if __name__ == "__main__":
    main()
