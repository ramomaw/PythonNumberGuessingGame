import random

random_number = random.randint(1, 100) 
guess_count = 0 
right_guess = 0

while right_guess != random_number:
    print("enter your guess between 1 and 100")
    right_guess = int(input()) 
    guess_count += 1
    if right_guess > random_number:
        print("your guess is bigger than the correct answer")
    elif right_guess < random_number:
        print("your guess is smaller than the correct answer")
else:
    print("you got the correct guess, your number of guesses are:")
    print(guess_count)