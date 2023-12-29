import random
def hangman_game():
    words = ['vehicle', 'america', 'onion', 'zombie', 'virus', 'athens', 'missisipi', 'information', 'kilobyte', 'wizard']
    riddle = random.choice(words)
    length = len(riddle)
    guessed_letters = ["_"] * length
    guesssed_correctly = False
    lives = 6

    print("Let's play Hangman")
    print("Drawn word has " + str(length) + " letters")

    while lives > 0:
        print("\n")
        print(" ".join(guessed_letters))


        guess = input("\n\nGuess the letter or whole word:   ")
        guess = guess.lower()

        if len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed this letter")
            elif guess in riddle:
                for i in range(length):
                    if riddle[i] == guess:
                        guessed_letters[i] = guess
                if "_" not in guessed_letters:
                    guesssed_correctly = True
                    break
                print("Good job, this letter is in the drawn word")
            else:
                lives -= 1
                print("Sadly incorrect. " + str(lives) + " lives ramaining")

        elif len(guess) == len(riddle):
            if guess == riddle:
                guesssed_correctly = True
                break
            else:
                lives -= 1
                print("Sadly incorrect. " + str(lives) + " lives ramaining")
        else:
            print("Wrong data, try again")

            print("\n")
    if guesssed_correctly:
        print("Congratulations, this is the correct answer. Your word is: " + str(riddle))
    else:
        print("Sadly, you loose")

hangman_game()
