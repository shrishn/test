def register_participants():
    # Get the number of participants
    try:
        num_participants = int(input("Enter the number of participants: "))
    except ValueError:
        print("Invalid Input")
        return
    
    # Validate input
    if num_participants <= 0:
        print("Invalid Input")
        return
    
    # Initialize dictionaries
    participant_preferences = {}
    event_participants = {'Workshop': [], 'Presentation': [], 'Hackathon': [], 'Quiz': []}
    
    # Loop to get participant details
    for _ in range(num_participants):
        name = input("Enter participant name: ").strip()
        email = input("Enter participant email: ").strip()
        reg_date = input("Enter registration date (YYYY-MM-DD): ").strip()
        preferences = input("Enter participant preferences separated by spaces (Workshop/Presentation/Hackathon/Quiz): ").strip().split()
        
        # Update participant preferences dictionary
        participant_preferences[name] = preferences
        
        # Update event participants dictionary
        for event in preferences:
            if event in event_participants:
                event_participants[event].append(name)
    
    print("Registered Successfully!")
    
    # Display the results
    print("\nParticipant Preferences:", participant_preferences)
    print("Event Participants:", event_participants)

# Run the program
register_participants()