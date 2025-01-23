# Get the age of the visitor from the user
print("Enter your age:")
age = int(input())  # Convert input to integer

# Check for invalid input
if age < 0:
    print("Invalid Input")
    exit(0)

# Determine ticket type and price based on age
if 0 <= age <= 12:
    ticket_type = "Child"
    ticket_price = 100.00
elif 13 <= age <= 64:
    ticket_type = "Adult"
    ticket_price = 200.00
else:  # Age 65 and above
    ticket_type = "Senior"
    ticket_price = 150.00

# Display the ticket details
print("\nTicket Details")
print(f"Type: {ticket_type}")
print(f"Ticket Price: Rs.{ticket_price:.2f}")
