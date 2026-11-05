# Caesar Cipher HC 1st
while True:
    alphabet = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    ]

    while True:
            try:
                mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
                if mode in ["encrypt", "decrypt"]:
                    break
            except ValueError:
                print("Invalid mode Please type 'encrypt' or 'decrypt'")

    while True:
            try:
                shift = int(input("What shift value would you like: "))
                break
            except ValueError:
                print("Invalid Input shift value must be a whole number")

    def encode(shift):

        shifted_alphabet = [alphabet[(i + shift) % 26 ] for i in range(26)]
        cipher_dict = dict(zip(alphabet, shifted_alphabet))

        text = input(f"Enter text to {mode}: ").lower()
        
        result_chars = []
        for char in text:
            if char in cipher_dict:
                result_chars.append(cipher_dict[char])
            else:
                result_chars.append(char)
                
        result_text = "".join(result_chars)
        
        print(f"\nInput text : {text}")
        print(f"Result text: {result_text}")

    def decode(shift):

        if mode == "decrypt":
            shift = -shift

        shifted_alphabet = [alphabet[(i + shift) % 26 ] for i in range(26)]
        cipher_dict = dict(zip(alphabet, shifted_alphabet))

        text = input(f"Enter text to {mode}: ").lower()
        
        result_chars = []
        for char in text:
            if char in cipher_dict:
                result_chars.append(cipher_dict[char])
            else:
                result_chars.append(char)
                
        result_text = "".join(result_chars)
        
        print(f"\nInput text : {text}")
        print(f"Result text: {result_text}")

    if mode == "encrypt":
        encode(shift)
    else:
        decode(shift)

    run_again = input("Would you like to run the program again? (yes/no): ").strip().lower()
    if run_again != "yes":
        break
