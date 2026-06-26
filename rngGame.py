import random
x = int(input("enter the lowest number:"))
y = int(input("enter the highest number:"))

if x > y:
    print(f"please enter a number bigger than {x}")
    y = int(input("enter the highest number"))

random_number = random.randint(x, y) 
guess_count = 0 
right_guess = 0

while right_guess != random_number:
    print(f"enter your guess between {x} and {y} ")
    right_guess = int(input()) 
    guess_count += 1
    if right_guess > random_number:
        print("your guess is bigger than the correct answer")
    elif right_guess < random_number:
        print("your guess is smaller than the correct answer")
else:
    print("you got the correct guess, your number of guesses are:")
    print(guess_count)