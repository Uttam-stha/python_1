import pandas as pd
import numpy as np

# Initializee empty DataFrame
columns = ["Roll_No", "Name", "Math", "Science","English", "Total", "Average", "Grade"]
df = pd.DataFrame(columns = columns)

# Function to calculate grade
def calculate_grade(avg):
    if avg >=90:
         return "A"
    elif avg >=75:
         return "B"
    elif avg >= 60:
         return "C"
    elif avg >= 40:
         return "D"
    else: return "F"

    # Add student
def add_student(roll,name, math, sci, eng):
     total = math + sci + eng
     avg = np.round(total / 3, 2)
     grade = calculate_grade(avg)
     global df
     df = pd.cancat([df, pd.DataFrame([[roll, name, math, sci, eng, total, avg, grade]], columns = columns)], ignore_index = True)

# Example usage
add_student(1, "Uttam", 85,90,70)
add_student(2, "Sujit",69, 70, 40 )

print(df)

# Save to CSV
df.to_csv("student_grades.csv", index=False)