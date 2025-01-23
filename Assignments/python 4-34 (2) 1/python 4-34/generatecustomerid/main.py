def generate_customer_id():
    # Get the number of customers
    try:
        num_customers = int(input("Enter the number of customers: "))
    except ValueError:
        print("Invalid input")
        return
    
    # If the number of customers is less than or equal to 0, display "Invalid input"
    if num_customers <= 0:
        print("Invalid input")
        return
    
    # Loop through each customer
    for i in range(num_customers):
        # Get the customer details
        customer_details = input(f"Enter the customer's details: ")
        
        # Split the details into name, date of birth, and location
        name, dob, location = customer_details.split("/")
        
        # Reverse the name and remove spaces
        reversed_name = name.replace(" ", "")[::-1]
        
        # Extract the year from the date of birth
        year = dob.split("-")[0]
        
        # Extract the first and last letters of the location
        location_code = location[0] + location[-1]
        
        # Extract the letters in even index positions of the reversed name
        even_index_name = "".join([reversed_name[i] for i in range(len(reversed_name)) if i % 2 == 0])
        
        # Generate the customer ID
        customer_id = even_index_name + year + location_code + str(i)
        
        # Display the customer ID
        print(f"Customer Id of {name} is {customer_id}")

# Call the function to generate customer IDs
generate_customer_id()
