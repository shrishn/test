class ProjectAllocation:
    def __init__(self, score_list):
        # Initialize the score_list attribute with the provided list
        self.score_list = score_list
        self.index = 0  # Initialize index for iteration
    
    def __iter__(self):
        # Return the iterator object itself
        return self
    
    def __next__(self):
        # Check if we have iterated through all employees
        if self.index < len(self.score_list):
            employee = self.score_list[self.index]
            employee_id = employee[0]
            scores = list(map(int, employee[1].split(',')))  # Convert score string to integers
            
            # Calculate average score
            average_score = sum(scores) / len(scores)
            
            # Increment the index for the next iteration
            self.index += 1
            
            # Return the dictionary with employee id and average score
            return {employee_id: round(average_score, 1)}
        else:
            # Stop iteration once all employees are processed
            raise StopIteration
