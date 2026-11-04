# Caesar Cipher HC 1st
# Caesar Cipher HC 1st
alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

def encode(text, shift):
    """Encodes the text by shifting letters forward, preserving case."""
    shifted_alphabet = [alphabet[(i + shift) % 26] for i in range(26)]
    cipher_dict = dict(zip(alphabet, shifted_alphabet))
    
    result_chars = []
    for char in text:
        if char.lower() in cipher_dict:
            # Shift the letter using its lowercase version
            shifted_char = cipher_dict[char.lower()]
            # Keep original capitalization
            result_chars.append(shifted_char.upper() if char.isupper() else shifted_char)
        else:
            result_chars.append(char)
            
    return "".join(result_chars)

def decode(text, shift):
    """Decodes the text by reusing encode logic with a negative shift."""
    return encode(text, -shift)

def caesar_cipher():
    """Main program flow to handle user input and call the correct function."""
    # This is the part where the user gets to choose if they want to encode or decode
    while True:
        mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
        if mode in ["encrypt", "decrypt"]:
            break
        print("Invalid mode. Please type 'encrypt' or 'decrypt'")

    # Asks how much they want to shift their word on the cipher by
    while True:
        try:
            shift = int(input("What shift value would you like: "))
            break
        except ValueError:
            print("Error: Shift value must be a whole number")

    # Gets what they want to decode or encode (removed .lower() to keep original text)
    text = input(f"Enter text to {mode}: ")

    # Calls the right function based on the chosen mode
    if mode == "encrypt":
        result_text = encode(text, shift)
    else:
        result_text = decode(text, shift)

    # Tells them their new word or decoded word
    print(f"\nInput text : {text}")
    print(f"Result text: {result_text}")

if __name__ == "__main__":
    caesar_cipher()
