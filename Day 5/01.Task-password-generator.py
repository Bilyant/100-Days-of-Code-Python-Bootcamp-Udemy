import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                      '-', '_', '=', '+', '[', ']', '{', '}', '.', ',',
                      '<', '>', '?']

print("Welcome to the Pypassword Generator")
letters_count = int(input("How many letter would you like in your password? "))
symbols_count = int(input("How many symbols would you like? "))
numbers_count = int(input("How many numbers would you like? "))

generated_password = []

for idx in range(letters_count):
    generated_password += random.choice(letters)
for idx in range(symbols_count):
    generated_password += random.choice(special_characters)
for idx in range(numbers_count):
    generated_password += str(random.choice(numbers))

random.shuffle(generated_password)

shuffled_password = ""
for idx in range(len(generated_password)):
    shuffled_password += generated_password[idx]

print(f"You generated password is: f{shuffled_password}")
