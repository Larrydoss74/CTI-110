"""
Larry Doss
4/19/2024
P5LAB
Leap Years
"""
def is_leap_year(year):
    """
    Determines if a given year is a leap year.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    # Get input from user
    year = int(input("Enter a year: "))

    # Check if it's a leap year
    if is_leap_year(year):
        print(f"{year} has **29 days** in February.")
    else:
        print(f"{year} has **28 days** in February.")

if __name__ == "__main__":
    main()
