from multipledispatch import dispatch

class Sports:
    
    @dispatch(int, int, int)
    def calculateScore(self, sixers, fours, singles):
        # Cricket Score Calculation
        score = (sixers * 6) + (fours * 4) + singles
        return score

    @dispatch(int, int, str)
    def calculateScore(self, white_pockets, black_pockets, red_pocket):
        # Carrom Score Calculation
        score = (white_pockets * 2) + (black_pockets * 1)
        if red_pocket.lower() == 'yes':
            score += 5
        return score

    @dispatch(int, int)
    def calculateScore(self, goals, fouls):
        # Basketball Score Calculation
        score = goals - fouls
        return score

def main():
    sport_type = input("Enter the type of sport (cricket, carrom, basketball): ").lower()
    sport = Sports()
    
    if sport_type == "cricket":
        sixers = int(input("Enter the number of sixers: "))
        fours = int(input("Enter the number of fours: "))
        singles = int(input("Enter the number of singles: "))
        score = sport.calculateScore(sixers, fours, singles)
        print(f"Calculated Score: {score}")
    
    elif sport_type == "carrom":
        white_pockets = int(input("Enter the number of white coins pocket: "))
        black_pockets = int(input("Enter the number of black coins pocket: "))
        red_pocket = input("Red Pocket(yes/no): ")
        score = sport.calculateScore(white_pockets, black_pockets, red_pocket)
        print(f"Calculated score: {score}")
    
    elif sport_type == "basketball":
        goals = int(input("Enter the number of goals: "))
        fouls = int(input("Enter the number of fouls: "))
        score = sport.calculateScore(goals, fouls)
        print(f"Calculated Score: {score}")
    
    else:
        print("Invalid sport type!")

if __name__ == "__main__":
    main()
