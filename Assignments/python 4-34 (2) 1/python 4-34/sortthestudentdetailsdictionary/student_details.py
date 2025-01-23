def main():
    student_details = []  # List to store student details as dictionaries
    
    while True:
        # Input the number of student details to be created
        try:
            num_students = int(input("Enter the no of student details to be created: "))
        except ValueError:
            print("Invalid Input")
            if student_details:
                print("Here's the list of student details :")
                for student in student_details:
                    print(student)
            break
        
        if num_students <= 0:
            print("Invalid Input")
            if student_details:
                print("Here's the list of student details :")
                for student in student_details:
                    print(student)
            break
        
        # Collect student details
        for _ in range(num_students):
            name = input("Name : ").strip()  # Remove any leading/trailing spaces
            try:
                age = int(input("Age : "))
            except ValueError:
                print("Invalid Input")
                if student_details:
                    print("Here's the list of student details :")
                    for student in student_details:
                        print(student)
                return
            
            # Check if age is valid
            if age < 10 or age > 80:
                print("Invalid Input")
                print("Here's the list of student details :")
                for student in student_details:
                    print(student)
                # Sort the student details by name
                student_details.sort(key=lambda x: x['Name'].lower())
                # Display the sorted student details
                print("\nHere's the list of student details sorted with respect to name :")
                for student in student_details:
                    print(student)
                return
            
            # Add the student's details to the list
            student_details.append({'Name': name, 'Age': age})
        
        # Ask if the admin wants to add more students
        try:
            add_more = int(input("Do you want to add more students' details to the list of dictionaries? If yes, press 1, else press 0: "))
        except ValueError:
            print("Invalid Input")
            # Display the student details before sorting
            print("\nHere's the list of student details :")
            for student in student_details:
                print(student)
            # Sort the student details by name
            student_details.sort(key=lambda x: x['Name'].lower())
            # Display the sorted student details
            print("\nHere's the list of student details sorted with respect to name :")
            for student in student_details:
                print(student)
            break
        
        if add_more == 0:
            # Display the student details before sorting
            print("\nHere's the list of student details :")
            for student in student_details:
                print(student)
            # Sort the student details by name
            student_details.sort(key=lambda x: x['Name'].lower())  # Sort case-insensitively
            # Display the sorted student details
            print("\nHere's the list of student details sorted with respect to name :")
            for student in student_details:
                print(student)
            break
        elif add_more != 1:
            print("Invalid Input")
            # Display the student details before sorting
            print("\nHere's the list of student details :")
            for student in student_details:
                print(student)
            # Sort the student details by name
            student_details.sort(key=lambda x: x['Name'].lower())
            # Display the sorted student details
            print("\nHere's the list of student details sorted with respect to name :")
            for student in student_details:
                print(student)
            break

if __name__ == '__main__':
    main()