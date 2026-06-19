import random

words = ("acid","ball","blow","bake","blue","cake","coin","dark","date","earn","ears","face","fake","fact","fear","fart","fast","fair","fail","gang","hall","icon","idle","jaws","jeep","lace","laid","lake","lamb","lame","lamp","land","made","maze","maid","mail","make","male","mall","many","milk","name","nail","nose","nike","nine","open","okay","pain","pace","play","pick","plot","rest","rain","rail","roll","soil","sail")
word = random.choice(words)
guess_word = ""
guess = 0
guess_limit = 12
out_of_guesses = False
while not(out_of_guesses) and guess_word != word:
    if guess < guess_limit:
        guess_word = input("Guess the word: ")
        guess += 1
        if guess_word != word:
            print("Wrong guess! Please try again.")

            # Show matching letters
            hint = ""
            for i in range(len(word)):
                if i < len(guess_word) and guess_word[i] == word[i]:
                    hint += word[i] + " "
                else:
                    hint += "_ "

            print("Hint:", hint)

    else:
        out_of_guesses = True
        hint = ""
if out_of_guesses:
    print("You have failed to guess the correct word!")
else:
    print("You have guessed the word correctly!")
    print(f"Number of guesses are {guess}")
