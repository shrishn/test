##Do not change the code skeleton given.  Write your program in the provided places alone.

def main():
    ### Write your code here
    
    # Input for the first list
    n1 = int(input())
    if n1 <= 0:
        print("Invalid list size")
        return
    all_doctors = []
    for _ in range(n1):
        doctor_id = int(input())
        if doctor_id <= 0:
            print("Invalid Id")
            return
        all_doctors.append(doctor_id)
    
    # Input for the second list
    n2 = int(input())
    if n2 <= 0:
        print("Invalid list size")
        return
    working_doctors = []
    for _ in range(n2):
        doctor_id = int(input())
        if doctor_id <= 0:
            print("Invalid Id")
            return
        working_doctors.append(doctor_id)
    
    # Find non-working doctors
    non_working_doctors = [doc for doc in all_doctors if doc not in working_doctors]
    
    # Output the result
    print("Not Working Doctors' IDs are:")
    print(*non_working_doctors)

if __name__ == '__main__':
    main()
