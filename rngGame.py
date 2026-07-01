import random

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")

def main():
    x = get_integer_input("Enter the lowest number: ")
    
    while True:
        y = get_integer_input("Enter the highest number: ")
        if y >= x:
            break
        print(f"Please enter a number greater than or equal to {x}.")

    random_number = random.randint(x, y) 
    guess_count = 0 
    right_guess = None

    print(f"\nA random number between {x} and {y} has been generated.")

    while right_guess != random_number:
        right_guess = get_integer_input(f"Enter your guess between {x} and {y}: ") 
        guess_count += 1
        
        if right_guess > random_number:
            print("Your guess is bigger than the correct answer.")
        elif right_guess < random_number:
            print("Your guess is smaller than the correct answer.")

    print(f"\nYou got the correct guess. Your total number of guesses is: {guess_count}")

if __name__ == "__main__":
    main()