def manage_toy_inventory():
    # Step 1: Read the content from the 'toys.txt' file
    try:
        with open('toys.txt', 'r') as file:
            existing_toys = file.readlines()
    except FileNotFoundError:
        print("The file 'toys.txt' does not exist.")
        return
    
    # Step 2: Create a new file 'new_toys.txt' and copy existing toys to it
    with open('new_toys.txt', 'w') as new_file:
        new_file.writelines(existing_toys)
    
    # Step 3: Take input for the number of new toys and collect their details
    try:
        num_new_toys = int(input("Enter the no. of new toys: "))
    except ValueError:
        print("Please enter a valid number for new toys.")
        return
    
    new_toys = []
    print("Enter the toy's details:")
    for _ in range(num_new_toys):
        toy_details = input()
        new_toys.append(toy_details + '\n')
    
    # Step 4: Append the new toy details to 'new_toys.txt'
    with open('new_toys.txt', 'a') as new_file:
        new_file.writelines(new_toys)
    
    # Step 5: Display the updated content of the new file
    print("\nUpdated toy inventory:")
    with open('new_toys.txt', 'r') as new_file:
        updated_content = new_file.readlines()
        for line in updated_content:
            print(line.strip())
    
    # Step 6: Calculate and display the total number of toys
    # Clean up any empty lines and count only actual toy entries
    total_toys = len([line for line in updated_content if line.strip()])
    print(f"\nNo. of toys: {total_toys}.")

# Call the function to manage the toy inventory
manage_toy_inventory()
