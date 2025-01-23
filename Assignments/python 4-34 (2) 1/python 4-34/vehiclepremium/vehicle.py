class Vehicle:
    def __init__(self, cost, type):
        # Private instance variables
        self.__cost = cost
        self.__type = type
        self.__premium = None

    # Method to calculate premium
    def calculate_premium(self):
        if self.__type == 1:
            # 2% of cost for Two Wheeler
            self.__premium = 0.02 * self.__cost
        elif self.__type == 2:
            # 6% of cost for Four Wheeler
            self.__premium = 0.06 * self.__cost
        elif self.__type == 3:
            # 8% of cost for Other types
            self.__premium = 0.08 * self.__cost

    # Getter method to return the premium
    def get_premium(self):
        return self.__premium


# Get input from the user
vehicle_cost = float(input("Enter the vehicle cost: "))
vehicle_type = int(input("Enter the type of the vehicles (1 for 2 wheeler, 2 for 4 wheeler and 3 for other types): "))

# Create an object of Vehicle class
vehicle_obj = Vehicle(vehicle_cost, vehicle_type)

# Calculate the premium amount
vehicle_obj.calculate_premium()

# Display the premium amount
print(f"The premium amount is: {vehicle_obj.get_premium()}")
