# Caesar Cipher HC 1st

alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

def caesar_cipher():
    """"This is the part where the user gets to choose if they want to encode or decode"""
    while True:
        mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
        if mode in ["encrypt", "decrypt"]:
            break
        print("Invalid mode. Please type 'encrypt' or 'decrypt'")

# Asks how much they want to shift there word on the cypher by
    while True:
        try:
            shift = int(input("What shift value would you like: "))
            break
        except ValueError:
            print("Error: Shift value must be a whole number")

# Reverses the direction of the shift if decrypt is selected so it will actually decrypt
    if mode == "decrypt":
        shift = -shift

#  Makes shifted library based on shift number and makes it into a dictionary using the og alphebet as well
    shifted_alphabet = [alphabet[(i + shift) % 26 ] for i in range(26)]
    cipher_dict = dict(zip(alphabet, shifted_alphabet))

# Gets what they want to decode or incode
    text = input(f"Enter text to {mode}: ").lower()
    
# Gets what each letter is on their word on the dictionary to encode or decode it
    result_chars = []
    for char in text:
        if char in cipher_dict:
            result_chars.append(cipher_dict[char])
        else:
            result_chars.append(char)
            
# Gives space in between words
    result_text = "".join(result_chars)
    
# Tells them there new word or decoded word
    print(f"\nnput text : {text}")
    print(f"Result text: {result_text}")


caesar_cipher()
