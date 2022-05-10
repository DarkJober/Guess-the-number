import random
from logo import logo

print(logo)

guessing_number = random.randint(1,100)
EASY_LEVEL_LIVES = 10
HARD_LEVEL_LIVES = 5

def difficulty():
    level = input("Choose your difficulty. 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_LIVES
    elif level == "hard":
        return HARD_LEVEL_LIVES

print("Welcome to the Richmond Road guessing game!")
print("I'm thinking of a number between 1 and 100")

turns = difficulty()

def game():
    global turns
    print(f"You have {turns} attempts remaining to guess the number.")
    while turns > 0:
        guess = int(input("Make a guess: "))
        if guess != guessing_number and turns == 1:
            turns = 0
            print(f"You've run out of guesses, you lose. Guessed number was {guessing_number}.")
        elif guess > guessing_number:
            turns -= 1
            print(f"Too high. You have {turns} left.")
        elif guess < guessing_number:
            turns -= 1
            print(f"Too low. You have {turns} left.")
        elif guess == guessing_number:
            print(f"You won. The guess was {guessing_number}")

game()