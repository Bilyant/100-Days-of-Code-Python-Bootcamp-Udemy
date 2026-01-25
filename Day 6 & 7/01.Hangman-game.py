import random

word_list = ["aardvark", "baboon", "camel"]

# TODO: Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

chosen_word = random.choice(word_list)
print(chosen_word)
guessed_word = []
for i in range(len(chosen_word)):
    guessed_word.append("-")
for char in guessed_word:
    print(char, end="")

# TODO: Ask the user to guess a letter and assign their answer to to a variable called guess. Make guess lowercase.
# TODO: Create a variable called "display" that puts the guess letter in the right position/s

guess = input("\nGuess a letter: ").lower()

for idx in range(len(chosen_word) - 1):
    if guess == chosen_word[idx]:
        guessed_word[idx] = guess


# TODO: Check if the letter the user guessed is one of the letters in the chosen_word. Print "Right" if it is.
#  "Wrong" if it's not.

# for letter in chosen_word:
#     if guess == letter:
#         print("Right")
#     else:
#         print("Wrong")

for char in guessed_word:
    print(char, end="")
