import json

def filter_customers(loan_type):
    try:
        # Step 1: Open and read the loan.json file
        with open('loan.json', 'r') as file:
            data = json.load(file)
        
        # Step 2: Flag to check if any customer matches the loan_type
        found = False
        
        # Step 3: Loop through customers and their loans to filter by loan_type
        for customer in data['customers']:
            for loan in customer['loans']:
                if loan['loan_type'].lower() == loan_type.lower():
                    # Step 4: If loan type matches, print the details
                    if not found:
                        print("Loan Details")
                        print("Account_Number     Customer_Name   Loan_Amount")
                        found = True
                    print(f"{customer['Account_Number']}       {customer['customer_name']}           {loan['loan_amount']}")
        
        # Step 5: If no matching customers found, display a message
        if not found:
            print("No customers available")
    
    except FileNotFoundError:
        print("The file 'loan.json' was not found.")
    except json.JSONDecodeError:
        print("Error decoding the JSON file.")

# Step 6: Get loan_type input from the user
loan_type = input("Enter the loan type\n")

# Call the function with the provided loan type
filter_customers(loan_type)