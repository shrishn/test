# Initialize variables to store votes
alice_votes = 0
bob_votes = 0
charlie_votes = 0

# Prompt for the number of voters
while True:
    try:
        num_voters = int(input("Enter the number of voters (1-100): "))
        if 1 <= num_voters <= 100:
            break
        else:
            print("Please enter a number between 1 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Loop to collect votes
for voter in range(1, num_voters + 1):
    while True:
        vote = input(f"Enter the vote for voter {voter} (Alice, Bob, or Charlie): ").strip()
        if vote.lower() == 'alice':
            alice_votes += 1
            break
        elif vote.lower() == 'bob':
            bob_votes += 1
            break
        elif vote.lower() == 'charlie':
            charlie_votes += 1
            break
        else:
            print("Invalid vote. Please enter a valid vote (Alice, Bob, or Charlie).")

# Calculate total votes and percentages
total_votes = alice_votes + bob_votes + charlie_votes
alice_percentage = (alice_votes / total_votes) * 100
bob_percentage = (bob_votes / total_votes) * 100
charlie_percentage = (charlie_votes / total_votes) * 100

# Display voting results
print("\nVoting Results:")
print(f"Candidate Alice received {alice_percentage:.2f}% of the votes.")
print(f"Candidate Bob received {bob_percentage:.2f}% of the votes.")
print(f"Candidate Charlie received {charlie_percentage:.2f}% of the votes.")

# Determine the winner
if alice_votes > bob_votes and alice_votes > charlie_votes:
    print("\nWinner: Candidate Alice")
elif bob_votes > alice_votes and bob_votes > charlie_votes:
    print("\nWinner: Candidate Bob")
elif charlie_votes > alice_votes and charlie_votes > bob_votes:
    print("\nWinner: Candidate Charlie")
else:
    print("\nIt's a tie! No clear winner.")
