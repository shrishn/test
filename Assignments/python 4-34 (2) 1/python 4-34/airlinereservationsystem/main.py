# Initialize variables
available_seats = 50
business_cost = 15000
economy_cost = 7500
total_booked_seats = 0
boarding_passes = []

print(f"Available Seats: {available_seats}")
print(f"Business Class: Rs.{business_cost} per seat")
print(f"Economy Class: Rs.{economy_cost} per seat\n")

while True:
    # Prompt for class choice
    while True:
        seat_class = input("Enter class (Business/Economy) for reservation: ").strip()
        if seat_class.lower() in ['business', 'economy']:
            break
        print("Invalid class choice. Please enter Business or Economy.\n")

    # Prompt for number of seats
    while True:
        seats_to_reserve = input("Enter the number of seats to reserve: ").strip()
        if not seats_to_reserve.isdigit():
            print("Invalid input. Please enter a valid number.\n")
            continue
        seats_to_reserve = int(seats_to_reserve)
        if seats_to_reserve > available_seats:
            print(f"Invalid number of seats. Available seats: {available_seats}\n")
            continue
        break

    # Calculate total cost
    if seat_class.lower() == 'business':
        cost_per_seat = business_cost
    else:
        cost_per_seat = economy_cost

    total_cost = seats_to_reserve * cost_per_seat
    available_seats -= seats_to_reserve
    total_booked_seats += seats_to_reserve

    # Add seats to boarding passes
    for i in range(total_booked_seats - seats_to_reserve + 1, total_booked_seats + 1):
        boarding_passes.append(f"Seat {i} - Boarding Pass")

    print(f"Reservation successful! Total cost: Rs.{total_cost}\n")

    # Check if user wants to make another reservation
    another_reservation = input("Do you want to make another reservation? (yes/no): ").strip().lower()
    if another_reservation == 'no':
        break

# Display boarding passes and thank-you message
print("\nBoarding Passes:")
for pass_info in boarding_passes:
    print(pass_info)

print("\nThank you for using our reservation system!")
