def main():
    # Take the number of students as input
    num_students = int(input("Enter the no. of students: "))
    
    if num_students <= 0:
        print("Invalid input")
        return
    
    # Initialize list to store each student's electives
    student_electives = []
    
    # Initialize a dictionary to count electives
    electives_count = {}
    
    # Collect electives preferences for each student
    for _ in range(num_students):
        electives = input("Enter electives: ").split('/')
        student_electives.append(electives)
        
        # Count the electives
        for elective in electives:
            if elective in electives_count:
                electives_count[elective] += 1
            else:
                electives_count[elective] = 1
    
    # Display student electives list
    print("Student electives list:", student_electives)
    
    # Display electives count
    print("Electives count:", electives_count)
    
    # Find common electives among all students
    common_electives = set(student_electives[0])
    
    for electives in student_electives[1:]:
        common_electives &= set(electives)
    
    # Display common electives or message if none found
    if common_electives:
        print("Common elective:", sorted(common_electives))
    else:
        print("No common electives found")

if __name__ == '__main__':
    main()
