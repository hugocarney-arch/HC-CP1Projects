# Caesar Cipher HC 1st

# Gets if they want to encode or decode
from ast import While


while True:
        mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
        if mode in ["encrypt", "decrypt"]:
            break
        else:
                print("Invalid mode Please type 'encrypt' or 'decrypt'")

# Gets how far they want to shift it and it will later be reversed if they want to decode so then it actually decodes
while True:
            try:
                shift = int(input("What shift value would you like: "))
                break
            except ValueError:
                print("Invalid Input shift value must be a whole number")

text = input(f"What word do you want to {mode}: ")

def encode(shift):
        shifted_text = [chr(ord(i) + shift % 26) for i in text]
        shifted_text = ''.join(shifted_text)

        print(f"\nInput text: {text}")
        print(f"Result text: {shifted_text}")

def decode(shift):
        # It makes a new alphebet based on the og alphebet and the shift number to find every letter reversed by the shift number
        shifted_word = [chr(ord(i) - shift % 26) for i in text]
        shifted_word = ''.join(shifted_word)
        
        print(f"\nInput text: {text}")
        print(f"Result text: {shifted_word}")

while True:
    # Uses the function neede based on what the user says the mode they want
    if mode == "encrypt":
        encode(shift)
        break
    else:
        decode(shift)
        break