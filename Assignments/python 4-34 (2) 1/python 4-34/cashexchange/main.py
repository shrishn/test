# Get user inputs
amount = int(input("Enter amount: "))
denomination_choice = int(input("Enter denomination choice (1 for Rs.100, 2 for Rs.200, 3 for Rs.500): "))

# Validate the amount
if amount <= 0:
    print("Invalid input")
    exit(0)

# Validate the denomination choice
if denomination_choice == 1:
    denomination_value = 100
elif denomination_choice == 2:
    denomination_value = 200
elif denomination_choice == 3:
    denomination_value = 500
else:
    print("Invalid input")
    exit(0)

# Check if the amount is less than the denomination value
if amount < denomination_value:
    print(f"Balance amount of Rs.{amount} has been returned.")
else:
    # Calculate the number of notes and the balance
    num_notes = amount // denomination_value
    balance = amount % denomination_value
    print(f"{num_notes}*Rs.{denomination_value} notes have been released in exchange for Rs.{amount}. Balance amount of Rs.{balance} has been returned.")
