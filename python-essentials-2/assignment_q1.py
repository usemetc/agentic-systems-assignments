class StudentMarks:
    def __init__(self, marks):
        self.marks = marks

    def last_three_avg(self):
        try:
            # Check if we have at least 3 marks
            if len(self.marks) < 3:
                # Manually raise an IndexError to be caught by the except block
                raise IndexError
            
            # Use negative indexing to slice the last three elements
            last_three = self.marks[-3:]
            avg = sum(last_three) / 3
            print(f"Average of last 3 marks is: {avg:.1f}")
            
        except IndexError:
            print("Not enough marks to calculate average")

# --- Example Usage ---
marks_list = [50, 60, 70, 80, 90]
student = StudentMarks(marks_list)
student.last_three_avg()