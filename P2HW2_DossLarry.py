"""
Larry Doss
3/16/24
P2HW2
Test Grades
"""

# Initialize an empty list to store the grades
gradesList = []

# Collect grades for each module (1 to 6)
for module in range(1, 7):
    try:
        # Prompt user for input
        grade = float(input(f"Enter grade for Module {module}: "))
        # Append grade to the list
        gradesList.append(grade)
    except ValueError:
        print("Invalid input. Please enter a valid numeric grade.")

# Calculate statistical data
lowestGrade = min(gradesList)
highestGrade = max(gradesList)
sumOfGrades = sum(gradesList)
averageGrade = sumOfGrades / len(gradesList)

# Display results
print(f"The lowest grade in the list: {lowestGrade}")
print(f"The highest grade in the list: {highestGrade}")
print(f"Sum of grades: {sumOfGrades}")
print(f"The grades’ average: {averageGrade:.2f}")
