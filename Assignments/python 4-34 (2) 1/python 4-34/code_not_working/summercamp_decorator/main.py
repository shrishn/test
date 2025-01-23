import re

# Decorator for email validation
def validate(func):
    def inner(candidates):
        valid_candidates = []
        
        # Regular expression for email validation
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        
        for candidate in candidates:
            name, age, email = candidate.split(':')
            if re.match(email_regex, email):  # Check if email is valid
                valid_candidates.append([name, int(age), email])
        
        # Call the original function with valid candidates
        return func(valid_candidates)
    
    return inner

# Segregate function to count participants in different age categories
@validate
def segregate(participants_list):
    under_10 = 0
    under_15 = 0
    under_20 = 0
    
    for participant in participants_list:
        name, age, email = participant
        if 5 <= age < 10:
            under_10 += 1
        elif 10 <= age < 15:
            under_15 += 1
        elif 15 <= age < 20:
            under_20 += 1
    
    # Return the counts for each category
    return under_10, under_15, under_20

# Main function to get user input and call segregate
def main():
    participants = []
    
    while True:
        candidate_details = input("Enter the candidate details as (name:age: email): ")
        participants.append(candidate_details)
        
        more = input("Do you want to enter another candidate's details(y/n): ")
        if more.lower() != 'y':
            break
    
    # Call segregate function which is decorated with validate
    under_10, under_15, under_20 = segregate(participants)
    
    # Display the results
    print(f"No. of participants under 10: {under_10}")
    print(f"No. of participants under 15: {under_15}")
    print(f"No. of participants under 20: {under_20}")

if __name__ == '__main__':
    main()
