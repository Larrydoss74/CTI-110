
"""
Larry Doss
3/3/24
P2Lab2
Simple Statistics
"""

# Input values (you can replace these with user inputs)
value1 = float(input("Enter the first value: "))
value2 = float(input("Enter the second value: "))
value3 = float(input("Enter the third value: "))
value4 = float(input("Enter the fourth value: "))

# Calculate product and average
product = value1 * value2 * value3 * value4
average = (value1 + value2 + value3 + value4) / 4

# Output rounded integers
print(f"Product (rounded): {product:.0f}")
print(f"Average (rounded): {average:.0f}")

# Output floating-point values with three decimal places
print(f"Product (floating-point): {product:.3f}")
print(f"Average (floating-point): {average:.3f}")
