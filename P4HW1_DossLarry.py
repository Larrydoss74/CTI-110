# Larry Doss
# 4/8/2024
# P4HW1 
# Grade Calculator

# Ask the user to enter the number of scores they want to input
num_scores = int(input("Enter the number of scores you'd like to enter: "))

# Initialize an empty list called "scores"
scores = []

# Collect scores from the user
for i in range(num_scores):
    while True:
        try:
            # Prompt the user to enter a score
            score = float(input(f"Enter score {i + 1}: "))
            # Validate if the score is within the range [0, 100]
            if 0 <= score <= 100:
                # Add the valid score to the "scores" list
                scores.append(score)
                break
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric score.")

# Find the lowest score in the "scores" list
lowest_score = min(scores)

# Remove the "lowest_score" from the "scores" list
scores.remove(lowest_score)

# Calculate the average of the remaining scores
average_score = sum(scores) / len(scores)

# Determine the letter grade for the calculated average
if 90 <= average_score <= 100:
    letter_grade = "A"
elif 80 <= average_score < 90:
    letter_grade = "B"
elif 70 <= average_score < 80:
    letter_grade = "C"
elif 60 <= average_score < 70:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display results
print(f"Lowest score entered: {lowest_score:.2f}")
print(f"Score List after dropping lowest score: {scores}")
print(f"The average of scores in modified list: {average_score:.2f}")
print(f"Letter grade for the calculated average: {letter_grade}")
