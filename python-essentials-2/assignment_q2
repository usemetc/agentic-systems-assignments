class StudentScores:
    def __init__(self, scores):
        self.scores = scores

    def highest_last_two(self):
        try:
            # We specifically check if there are fewer than 2 scores
            if len(self.scores) < 2:
                raise IndexError
            
            # Slice from the second-to-last item to the end
            last_two = self.scores[-2:]
            highest = max(last_two)
            
            print(f"Highest score among last two is: {highest}")
            
        except IndexError:
            print("Not enough scores to find highest value")

# --- Example Usage ---
scores_list = [45, 67, 89, 72]
student = StudentScores(scores_list)
student.highest_last_two()