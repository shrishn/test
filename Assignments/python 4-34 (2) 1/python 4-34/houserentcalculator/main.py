# Initialize the total rent for all tenants
total_rent = 0

while True:
    # Prompt user for house type or to quit
    house_type = int(input("Enter the type of house (1 BHK / 2 BHK / 3 BHK) or 0 to quit: "))

    # Check if user wants to quit
    if house_type == 0:
        break

    # Determine base rent based on house type
    if house_type == 1:
        base_rent = 1000
    elif house_type == 2:
        base_rent = 1500
    elif house_type == 3:
        base_rent = 2000
    else:
        print("Invalid house type. Please enter 1, 2, 3, or 0 to quit.")
        continue

    # Prompt for parking and cleaning services
    parking_required = int(input("Parking required? (1/0): "))
    cleaning_required = int(input("Special cleaning services required? (1/0): "))

    # Calculate additional charges
    if parking_required == 1 and cleaning_required == 1:
        additional_charges = 150
    elif parking_required == 1:
        additional_charges = 100
    elif cleaning_required == 1:
        additional_charges = 50
    else:
        additional_charges = 0

    # Calculate total rent for the tenant
    tenant_rent = base_rent + additional_charges
    print(f"Rent after including additional charges: {tenant_rent}")

    # Add tenant's rent to total rent
    total_rent += tenant_rent

# Display total rent and thank-you message
print(f"Total rent: {total_rent}")
print("Thank you for using our application!")
