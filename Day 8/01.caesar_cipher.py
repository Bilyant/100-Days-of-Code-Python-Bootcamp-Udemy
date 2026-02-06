import logo

print(logo.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for char in original_text:
        index = alphabet.index(char) + shift_amount
        index %= len(alphabet)
        encrypted_text += alphabet[index]
    return encrypted_text

encrypted_message = encrypt(text, shift)

print(f"Here is the encoded result: {encrypted_message}")
