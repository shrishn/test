# Import the ProjectAllocation class from allocation.py
from allocation import ProjectAllocation

def main():
    # Accept the number of employees
    num_employees = int(input("Enter the no. of employees: "))
    
    # Create a list to store employee data
    score_list = []
    
    # Loop through to accept employee data
    for _ in range(num_employees):
        employee_id = input("Enter the employee id: ")
        scores = input("Enter the scores of 5 assessments (comma separated) for the employee: ")
        score_list.append([employee_id, scores])
    
    # Create an object of ProjectAllocation with the collected score_list
    project_allocation = ProjectAllocation(score_list)
    
    # Display the results using the iterator
    print("Employees' average scores:")
    for avg_score in project_allocation:
        print(avg_score)

if __name__ == '__main__':
    main()
