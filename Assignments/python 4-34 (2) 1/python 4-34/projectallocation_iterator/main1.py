#DO NOT CHANGE THE CODE TEMPLATE GIVEN.  WRITE YOUR CODE IN THE PROVIDED PLACES ALONE
    
#import necessary modules here
from allocation import ProjectAllocation

def main():
    # Write your code here for getting user inputs, creating object for the custom iterator 'ProjectAllocation', 
    # and displaying the result using iterator.
    
    num_employees = int(input("Enter the number of employees: "))
    score_list = []

    for _ in range(num_employees):
        employee_id = input("Enter the employee id: ")
        scores = input("Enter the scores of 5 assessments (comma separated) for the employee: ").split(',')
        score_list.append([employee_id] + scores)

    project_allocation = ProjectAllocation(score_list)
    print("Employees' average scores:")
    for employee_avg in project_allocation:
        print(employee_avg)
    
    return None 

if __name__ == '__main__' : 
    main()
