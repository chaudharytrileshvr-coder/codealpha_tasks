import random


words = ["python", "tbilisi", "lucknow", "travel", "georgia"]


secret_word = random.choice(words)
guessed_letters = []  
incorrect_guesses = 0
max_incorrect = 6

print("=== Welcome to Hangman Game ===")
print("You have to guess a word, one letter at a time.")
print(f"You have {max_incorrect} incorrect guesses available.\n")



while incorrect_guesses < max_incorrect:
   
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print(f"Word: {display_word}")
    print(f"Guessed letters: {guessed_letters}")
    print(f"Galat attempts bache: {max_incorrect - incorrect_guesses}")

  
    if all(letter in guessed_letters for letter in secret_word):
        print(f"\nCongratulations! you won! Word is: {secret_word}")
        break

    
    guess = input("guess one letter: ").lower()

  
    if len(guess) != 1 or not guess.isalpha():
        print("write a single letter!\n")
        continue
    if guess in guessed_letters:
        print("this letter has already been guessed!\n")
        continue

    guessed_letters.append(guess)

    
    if guess in secret_word:
        print("right!\n")
    else:
        incorrect_guesses += 1
        print(f"wrong! {guess} it is not in the word.\n")

else:
    
    print(f"\nGame Over! you lost the game. right word was: {secret_word}")