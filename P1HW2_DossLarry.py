"""
Larry Doss
2/22/24
P1HW2
Travel Expense
"""



# Get the user's budget
budget = float(input("Enter your budget: "))

# Get the travel destination
destination = input("Enter your travel destination: ")

# Get the amount for gas expenses
gas_expenses = float(input("How much do you think you will spend on gas? "))

# Get the amount for accommodation expenses
accommodation_expenses = float(input("Approximately how much will you need for accommodation/hotel? "))

# Get the amount for food expenses
food_expenses = float(input("Last, how much do you need for food? "))

# Calculate total expenses
total_expenses = gas_expenses + accommodation_expenses + food_expenses

# Calculate remaining balance
remaining_balance = budget - total_expenses

# Display results
print("\n----------- Travel Expenses -----------")
print(f"Location: {destination}")
print(f"Initial Budget: ${budget:.2f}")
print(f"Fuel: ${gas_expenses:.2f}")
print(f"Accommodation: ${accommodation_expenses:.2f}")
print(f"Food: ${food_expenses:.2f}\n")
print(f"Remaining Balance: ${remaining_balance:.2f}")
