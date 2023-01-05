# random module should be imported, as a first step.
import random

# The player should input a number to determine the outbound/maximum of the range.
top_of_range = input("Type a number: ")

# The type of the input should be made sure that is digit and larger than 0.
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please, type a number larger than 0 next time! ")
        quit()

else:
    print("Please, type a number next time! ")
    quit()

# random module can be used in two functions: random.randint() and random.randrange().
# top_of_range function is put in as a outbound/maximum of the range.
random_number = random.randint(0, top_of_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number! ")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")


if guesses > 1:
    print(f"You got it in {guesses} guesses!")
else:
    print(f"You got it in {guesses} guess!")
