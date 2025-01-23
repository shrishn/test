import numpy as np

def main():
    # Create an empty list to store points for each quarter
    john_points = []

    # Get user input for each quarter
    print("Enter John's points for each quarter:")

    # Loop through each quarter (4 quarters)
    for quarter in range(1, 5):
        quarter_points = []
        for point in range(1, 5):  # 4 points per quarter
            score = int(input(f"Quarter {quarter}, Point {point}: "))
            quarter_points.append(score)  # Add each point to the current quarter
        john_points.append(quarter_points)  # Add the points of the current quarter to the john_points list

    # Convert the list of points into a numpy array
    john_statistics = np.array(john_points)

    # Ensure the john_statistics array has been populated correctly
    print("\nJohn's Statistics:")
    print(john_statistics)

    # Calculate the total points scored by John in the first two quarters
    total_points_first_two_quarters = np.sum(john_statistics[:2])

    # Calculate the average points scored by John in the last quarter
    average_points_last_quarter = np.mean(john_statistics[3])

    # Display the results
    print(f"\nTotal points scored by John in the first 2 quarters : {total_points_first_two_quarters:.2f}")
    print(f"Average points scored by John in the last quarter: {average_points_last_quarter:.2f}")

if __name__ == '__main__':
    main()
