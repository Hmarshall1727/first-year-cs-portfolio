import random # required for randint()

# Set the range of values allowed

MINIMUM_VALUE = 62
MAXIMUM_VALUE = 69

MAXIMUM_GUESSES = 9


# Generate a random number in the given range


target_value = random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
#print(f"The target value is {target_value}")

number_of_guesses = 0
players_guess = -1


while number_of_guesses < MAXIMUM_GUESSES and players_guess != target_value:


    number_of_guesses = number_of_guesses + 1
    players_guess = int(input(f"Enter your guess {MINIMUM_VALUE} to {MAXIMUM_VALUE} "))

    #print(f"Guess number {number_of_guesses} was {players_guess}")
     
    number_of_guesses = number_of_guesses + 1
    players_guess = int(input(f"Your guess {players_guess} is too low."))
    
    if players_guess < target_value:
       print(f"Your guess {players_guess} is too low.")
    elif players_guess > target_value:
         print(f"Your guess {players_guess} is too high.")
    else:
         print(f"Your guess {players_guess} is correct!")


print()
print(f"Game Over Player One")
