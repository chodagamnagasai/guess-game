import random

words = ("pilot","aeroplane","bike","sneeze","guess","door","wind","helmet","vase","pot")
word = random.choice(words)
guess_word = ""
guess = 0
guess_limit = 10
out_of_guesses = False
while not(out_of_guesses) and guess_word != word:
    if guess < guess_limit:
        guess_word = input("Guess the word: ")
        guess += 1
        if guess_word != word:
            print("Wrong guess! please try again_/\_ ")
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You have failed to guess the correct word!")
else:
    print("You have guessed correctly!")
    print(f"Number of guesses are {guess}")
