"""
Larry Doss
3/18/24
P3LAB
Leap Year
"""

def is_leap_year(year):
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        return True
    else:
        return False

# Get input from the user
year = int(input("Enter a year: "))

# Check if it's a leap year
if is_leap_year(year):
    print(f"{year} - leap year")
else:
    print(f"{year} - not a leap year")
