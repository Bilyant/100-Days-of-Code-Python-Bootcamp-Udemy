import art

def caesar(action, original_text, shift_amount):
    message = ""

    if action == 'decode':
        shift_amount *= -1

    for char in original_text:
        if char not in alphabet:
            message += char
            continue

        index = alphabet.index(char) + shift_amount
        index %= len(alphabet)
        message += alphabet[index]
    print(f"Here is the {action}d result: {message}")

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
is_solved = False

while not is_solved:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ['encode', 'decode']:
        print("Please type a valid answer.")
        continue
        
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)

    to_continue = input("Would you like to continue? Type 'Yes' or 'No'\n").lower()
    if to_continue == 'no':
        is_solved = True
        print("Goodbye")
