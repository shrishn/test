# Prompt the user to input the number of days
num_days = int(input("Enter the number of days: "))

# Check for invalid input
if num_days <= 0:
    print("Invalid input: No data entered.")
else:
    steps = []
    for day in range(1, num_days + 1):
        step_count = int(input(f"Enter the number of steps for Day {day}: "))
        steps.append(step_count)

    # Calculate the average steps per day
    avg_steps = sum(steps) / num_days

    # Find the day with the most and least steps
    max_steps = max(steps)
    min_steps = min(steps)
    max_day = steps.index(max_steps) + 1
    min_day = steps.index(min_steps) + 1

    # Check for consecutive increasing and decreasing streaks
    increasing_streak = all(steps[i] < steps[i + 1] for i in range(num_days - 1))
    decreasing_streak = all(steps[i] > steps[i + 1] for i in range(num_days - 1))

    # Display analysis results
    print("\nAnalysis Results:")
    print(f"Average steps per day: {avg_steps:.2f}")
    print(f"Day with the most steps: Day {max_day} ({max_steps} steps)")
    print(f"Day with the least steps: Day {min_day} ({min_steps} steps)")
    print(f"Consecutive increasing steps streak: {'Yes' if increasing_streak else 'No'}")
    print(f"Consecutive decreasing steps streak: {'Yes' if decreasing_streak else 'No'}")
