import random
import hangman_art
import hangman_words

lives = 7
print("\nWelcome to ")
print(hangman_art.logo)
print("Enjoy and good luck!\n")
print("-" * 40)
hangman_progress = -1
chosen_word = random.choice(hangman_words.words)
# print(chosen_word)
guessed_word = ["_" for char in range(len(chosen_word))]
used_letters = []
print(f"Word to guess: {''.join(guessed_word)}")

guesses = 0
game_over = False

while not game_over or guessed_word == chosen_word:
    if len(used_letters) > 0:
        print(f"Letters used so far: {', '.join(used_letters)}")
    letters_guessed = ", ".join(guessed_word)
    print(f"You have *****  {lives}/7  ***** lives left.")
    guess = input("Guess a letter: ").lower()
    used_letters.append(guess)
    if guess in guessed_word:
        print(f"You've already guessed '{guess}'. Please try with a different letter.")

    guesses += 1
    guessed_right = False
    for idx in range(len(chosen_word)):
        if guess == chosen_word[idx]:
            guessed_word[idx] = guess
            guessed_right = True
    for char in guessed_word:
        print(char, end="")

    if not guessed_right:
        hangman_progress += 1
        lives -= 1
        print("\nYou guessed wrong. You lose a life.")
    print(hangman_art.hangman[hangman_progress])

    formed_word = "".join(guessed_word)
    is_guessed = formed_word == chosen_word

    if hangman_progress == len(hangman_art.hangman) - 1 or is_guessed:
        game_over = True
        if is_guessed:
            print("\n***** You win! *****")
        else:
            print("\n*****  You lose!  *****")
            print(f"The word was: {chosen_word}")
