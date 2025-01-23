def update_salaries_and_search():
    # Open the file and read the contents
    with open('employee.txt', 'r') as file:
        employees = file.readlines()
    
    updated_employees = []
    
    # Update the salary by 10% for each employee
    for employee in employees:
        emp_id, emp_name, emp_salary = employee.strip().split(',')
        emp_salary = float(emp_salary)
        updated_salary = round(emp_salary * 1.10, 2)  # 10% increment, rounded to 2 decimal places
        updated_employees.append(f"{emp_id},{emp_name},{updated_salary:.2f}")
    
    # Overwrite the file with updated salaries
    with open('employee.txt', 'w') as file:
        for updated_employee in updated_employees:
            file.write(updated_employee + '\n')
    
    # Display updated details
    print("The updated details are:")
    for updated_employee in updated_employees:
        print(updated_employee)
    
    # Take input for employee ID to search
    search_id = input("\nEnter the employee id: ")
    
    # Search for the employee by ID
    found = False
    for updated_employee in updated_employees:
        emp_id, emp_name, emp_salary = updated_employee.split(',')
        if emp_id == search_id:
            print(f"The employee {emp_name} with id {emp_id} has salary Rs.{emp_salary}")
            found = True
            break
    
    if not found:
        print("No records found")

# Call the function to run the program
update_salaries_and_search()
