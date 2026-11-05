# Caesar Cipher HC 1st

# Gets if they want to encode or decode
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

text = input(f"What word do you want to {mode}:")

def encode(shift):
        """It first makes a alphebet with all the letters in alphebet to that is shifted with the shift number then it makes it into a new dictionary thata lines up every letter in alphetbet with its match that has been shifted in the shifted alphebet"""
        shifted_text = [chr(ord(text) + shift % 26 )]

        print(f"\nInput text : {text}")
        print(f"Result text: {shifted_text}")

def decode(shift):
        """It takes a word and the shift number but reverses the shift numbers so it goes backwards so it is decoding"""
        if mode == "decrypt":
            shift = -shift

        # It makes a new alphebet based on the og alphebet and the shift number to find every letter reversed by the shift number
        shifted_word = [chr(ord(text) + shift % 26 )]
        
        print(f"\nInput text : {text}")
        print(f"Result text: {shifted_word}")

while True:

    # Uses the function neede based on what the user says the mode they want
    if mode == "encrypt":
        encode(shift)
    else:
        decode(shift)

    # Asks if they want to restart the cipher to do it again and if they say anything except yes it will end the program/loop
    run_again = input("Would you like to run the program again? (yes/no): ").strip().lower()
    if run_again != "yes":
        break
