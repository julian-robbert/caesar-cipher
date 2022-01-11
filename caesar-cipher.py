alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

def caesar(start_text, shift_amount, direction):
    shift_amount %= 26
    end_text = ""
    for letter in start_text:
        if not letter.isalpha():
            end_text += letter
            continue
        index = alphabet.index(letter)
        if direction == "encode":
            new_letter = alphabet[index + shift_amount]
        elif direction == "decode":
            new_letter = alphabet[index - shift_amount]
        end_text += new_letter
    print(f"Your {direction}d text is: {end_text}")

repeat = "y"
while repeat == "y":
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    repeat = input("Would you like to restart the program? (Y or N): ").lower()