import random
from wordlist import words
from art import logo, hangman, thanks

# Game Screen
print(logo)
print(
    "--------- Created by Samyak Piya: https://www.linkedin.com/piyasamyak ----------"
)
print()


continueGame = True
while continueGame == True:
    lives = 6
    blanks = []
    guessed = []

    # Choose a random lowercase English word and create blank spaces equal to the word length
    word = random.choice(words)
    for i in range(len(word)):
        blanks.append("__")

    print(
        "--------------------------------------------------------------------------------"
    )
    print(
        f"A new {len(word)} digit word has been generated. The game has begun. Good Luck!"
    )
    print(
        "--------------------------------------------------------------------------------"
    )
    print("NOTE: You only have a total of 6 guesses for the word.")
    while lives > 0 and ("__" in blanks):
        # Display Game Status
        print(hangman[lives])
        print(" ".join(blanks))
        print()

        guess = input("Guess a letter in the word: ")

        # Check if the guess was correct
        if guess in guessed:
            print()
            print("You have already guessed this letter. Please choose another one!")
            guess = input("Guess a different letter in the word: ")

        # Add guessed letters to a list to remember previous letter inputs from the user
        guessed.append(guess)

        isCorrectGuess = False
        for i in range(len(word)):
            if guess == word[i]:
                isCorrectGuess = True
                blanks[i] = guess

        if isCorrectGuess == False:
            lives -= 1
            print(
                f"The letter '{guess}'' does not exist in the word. You have {lives} chances remaining."
            )
        else:
            print(f"Good one! The letter '{guess}' does exist in the word.")

    print()

    # When the user loses
    print(
        "--------------------------------------------------------------------------------"
    )
    if lives == 0:
        print(hangman[lives])
        play = input(
            f"You lost! The word was '{word}'. Do you want to continue playing? Type 'yes' or 'no'.\n-> "
        ).lower()
    else:
        play = input(
            f"You won! The word was indeed '{word}'. Do you want to continue playing? Type 'yes' or 'no'.\n-> "
        ).lower()
    print(
        "--------------------------------------------------------------------------------"
    )

    # When the user wants to quit
    if play == "no":
        continueGame = False
        print(thanks)
