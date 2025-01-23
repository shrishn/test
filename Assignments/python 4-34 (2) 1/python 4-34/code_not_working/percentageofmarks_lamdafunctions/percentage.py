def main():
    # Get marks for three subjects from the user
    subject1 = int(input("Enter marks for subject1: "))
    subject2 = int(input("Enter marks for subject2: "))
    subject3 = int(input("Enter marks for subject3: "))

    # Define the lambda function to calculate percentage
    cal = lambda sub1, sub2, sub3: (sub1 + sub2 + sub3) / 3

    # Calculate the percentage using the lambda function
    percentage = cal(subject1, subject2, subject3)

    # Display the result
    print(f"Percentage is {percentage:.1f}")

if __name__ == '__main__':
    main()
