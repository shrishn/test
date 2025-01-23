def main():
    # Input the number of employees
    num_employees = int(input("Enter no. of employees: "))
    
    # Check for invalid input
    if num_employees <= 0:
        print("Invalid input")
        return
    
    # Initialize an empty list to store employee details
    employee_details = []
    
    # Collect details for each employee
    for _ in range(num_employees):
        name = input("Enter name: ")
        sales = int(input("Enter no of products sold: "))
        city = input("Enter city: ")
        
        # Add the employee details as a dictionary to the list
        employee_details.append({'name': name, 'sales': sales, 'city': city})
    
    # Initialize an empty dictionary to group employees by city
    city_sales = {}
    
    # Group the employees' sales by city
    for employee in employee_details:
        city = employee['city']
        if city not in city_sales:
            city_sales[city] = [{'name': employee['name'], 'sales': employee['sales']}]
        else:
            city_sales[city].append({'name': employee['name'], 'sales': employee['sales']})
    
    # Display the grouped dictionary
    print(city_sales)

if __name__ == '__main__':
    main()
