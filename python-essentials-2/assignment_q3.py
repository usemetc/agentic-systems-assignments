class StudentPerformance:
    def __init__(self, scores):
        self.scores = scores

    def score_difference(self):
        try:
            # Attempting to access index 0 will fail if the list is empty
            if not self.scores:
                raise IndexError
            
            first_score = self.scores[0]
            last_score = self.scores[-1]
            
            difference = last_score - first_score
            print(f"Difference between last and first score is: {difference}")
            
        except IndexError:
            print("No scores available to calculate difference")

# --- Example Usage ---
scores_list = [55, 65, 75, 85]
student = StudentPerformance(scores_list)
student.score_difference()