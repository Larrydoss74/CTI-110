"""
Larry Doss
4/19/24
P4HW2
Pay Calculator
"""

# Initialize variables to keep track of totals
total_regular_pay = 0
total_overtime_pay = 0
total_employees = 0

# Sentinel value to terminate the program
SENTINEL = "Done"

# Main loop to collect employee information
while True:
    # Ask for employee name
    employee_name = input("Enter employee name (or 'Done' to finish): ")
    
    # Check if user wants to terminate the program
    if employee_name.lower() == SENTINEL.lower():
        break
    
    # Ask for pay rate and hours worked
    try:
        pay_rate = float(input("Enter pay rate (per hour): "))
        hours_worked = float(input("Enter hours worked: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue
    
    # Calculate regular pay (up to 40 hours)
    if hours_worked <= 40:
        regular_pay = hours_worked * pay_rate
        overtime_pay = 0
        overtime_hours = 0  # No overtime hours
    else:
        # Calculate overtime pay (hours worked beyond 40)
        regular_pay = 40 * pay_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (1.5 * pay_rate)
    
    # Calculate gross pay (regular pay + overtime pay)
    gross_pay = regular_pay + overtime_pay
    
    # Update totals
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_employees += 1

# Display results
print("\nResults:")
print(f"Total regular pay: ${total_regular_pay:.2f}")
print(f"Total overtime pay: ${total_overtime_pay:.2f}")
print(f"Total gross pay: ${gross_pay:.2f}")
print(f"Number of employees entered: {total_employees}")
