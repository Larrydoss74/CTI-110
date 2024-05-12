"""
Larry Doss
3/24/24
P3HW2
Salary
# Pseudocode for Employee Pay Calculator
"""

# Prompt the user for the employee's name
employee_name = input("Enter the employee's name: ")

# Prompt the user for the number of hours worked this week
hours_worked = float(input("Enter the number of hours worked this week: "))

# Prompt the user for the employee's pay rate
pay_rate = float(input("Enter the employee's pay rate: "))

# Calculate overtime pay if applicable
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
else:
    overtime_hours = 0
    overtime_pay = 0

# Calculate regular pay
regular_hours = hours_worked - overtime_hours
regular_pay = regular_hours * pay_rate

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display the results
print("\nEmployee Name:", employee_name)
print("Pay Rate: $", pay_rate)
print("Hours Worked:", hours_worked)
print("Overtime Hours:", overtime_hours)
print("Overtime Pay: $", overtime_pay)
print("Pay for Regular Hours: $", regular_pay)
print("Gross Pay: $", gross_pay)
