"""
Larry Doss
3/16/24
P2HW1
Travel Expenses
"""
print("This program calculates and displays travel expenses")
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
fuel = float(input("How much do you think you will spend on gas? "))
accommodation = float(input(f"Approximately, how much will you need for accommodation/hotel in {destination}? "))
food = float(input("Last, how much do you need for food? "))

remaining_balance = budget - fuel - accommodation - food

print(f"""
--------Travel Expenses--------
Location:          {destination}
Initial Budget:    ${budget:.2f}
Fuel:              ${fuel:.2f}
Accommodation:      ${accommodation:.2f}
Food:              ${food:.2f}
--------------------------------
Remaining Balance: ${remaining_balance:.2f}
""")
