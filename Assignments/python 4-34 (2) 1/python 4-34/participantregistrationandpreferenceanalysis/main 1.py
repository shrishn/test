# Prompt the user to input the number of participants for the event
num_participants = int(input("Enter the number of participants: "))

# Check if the number of participants is zero or negative
if num_participants <= 0:
    print("Invalid Input")
    exit()

# Initialize dictionaries to store participant preferences and event participants
participant_preferences = {}
event_participants = {}

# Loop through each participant to get their details
for _ in range(num_participants):
    name = input("Enter participant name: ")
    email = input("Enter participant email: ")
    registration_date = input("Enter registration date(YYYY-MM-DD): ")
    preferences = input("Enter participant preferences separated by spaces (Workshop/Presentation/Hackathon/Quiz): ").split()
    
    # Update participant preferences dictionary
    participant_preferences[name] = preferences
    
    # Update event participants dictionary
    for event in preferences:
        if event not in event_participants:
            event_participants[event]=[]
            event_participants[event].append(name)

# Display the results
print("Registered Successfully!")
print("Participant Preferences:",participant_preferences)
print("Event Participants:",event_participants)

