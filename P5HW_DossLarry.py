"""
Larry Doss
4/28/24
P5HW
Math Quiz
"""
import random

def generate_random_numbers():
    return random.randint(1, 100), random.randint(1, 100)

def add_numbers():
    num1, num2 = generate_random_numbers()
    actual_sum = num1 + num2
    attempts = 0

    while True:
        print(f"Add the following numbers: {num1} + {num2}")
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess == actual_sum:
            print(f"Congratulations! Your guess is correct. It took you {attempts} attempts.")
            break
        elif user_guess < actual_sum:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")

def main():
    print("Welcome to Math Quiz!")
    while True:
        print("\nMENU:")
        print("1. Add two random numbers")
        print("2. Subtract two random numbers")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_numbers()
        elif choice == '2':
            # Implement the subtract_numbers() function
            pass
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
