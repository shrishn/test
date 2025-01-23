import numpy as np 
points = []
print("Enter John's poits for each quarter:")
for quarter in range(1,5):
    quarter_points = [] 
    for point in range(1,5):
        score = int(input(f"Quarter {quarter}, Point {point}:"))
        quarter_points.append(score)
    points.append(quarter_points)
    
john_statistics = np.array(points)

total_points_first_two_quarters = np.sum(john_statistics[:2])

average_points_last_quarter = np.mean(john_statistics[3])

print("\nJohn's Statistics:")
print(john_statistics)
print(f"\nTotal points scored by John in the first 2 quarters:{total_points_first_two_quarters:.2f}")
print(f"Average points scored by John in the last quarter: {average_points_last_quarter:.2f}")