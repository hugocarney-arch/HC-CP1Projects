# Caesar Cipher HC 1st

while True:
    alphabet = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    ]

    # Gets if they want to encode or decode
    while True:
            try:
                mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
                if mode in ["encrypt", "decrypt"]:
                    break
            except ValueError:
                print("Invalid mode Please type 'encrypt' or 'decrypt'")

    # Gets how far they want to shift it and it will later be reversed if they want to decode so then it actually decodes
    while True:
            try:
                shift = int(input("What shift value would you like: "))
                break
            except ValueError:
                print("Invalid Input shift value must be a whole number")

    def encode(shift):
        """It first makes a alphebet with all the letters in alphebet to that is shifted with the shift number then it makes it into a new dictionary thata lines up every letter in alphetbet with its match that has been shifted in the shifted alphebet"""
        shifted_alphabet = [alphabet[(i + shift) % 26 ] for i in range(26)]
        cipher_dict = dict(zip(alphabet, shifted_alphabet))

        text = input(f"Enter text to {mode}: ").lower()
        
        # Takes word hen it compares it to the new cipher dict to make the new encoded word
        result_characters = []
        for characters in text:
            if characters in cipher_dict:
                result_characters.append(cipher_dict[characters])
            else:
                result_characters.append(characters)
                
        result_text = "".join(result_characters)
        

        print(f"\nInput text : {text}")
        print(f"Result text: {result_text}")

    def decode(shift):
        """It takes a word and the shift number but reverses the shift numbers so it goes backwards so it is decoding"""
        if mode == "decrypt":
            shift = -shift

        # It makes a new alphebet based on the og alphebet and the shift number to find every letter reversed by the shift number
        shifted_alphabet = [alphabet[(i + shift) % 26 ] for i in range(26)]
        cipher_dict = dict(zip(alphabet, shifted_alphabet))

        text = input(f"Enter text to {mode}: ").lower()
        
        # It does the same thing it does in the encode function
        result_characters = []
        for characters in text:
            if characters in cipher_dict:
                result_characters.append(cipher_dict[characters])
            else:
                result_characters.append(characters)
                
        result_text = "".join(result_characters)
        
        print(f"\nInput text : {text}")
        print(f"Result text: {result_text}")

    # Uses the function neede based on what the user says the mode they want
    if mode == "encrypt":
        encode(shift)
    else:
        decode(shift)

    # Asks if they want to restart the cipher to do it again and if they say anything except yes it will end the program/loop
    run_again = input("Would you like to run the program again? (yes/no): ").strip().lower()
    if run_again != "yes":
        break
