"""# H.C String Methods Notes

sentence = "The quick brown fox jumps over the lazy dog"

word = input("What word do you want: ").strip().lower()
new_word = input(" What word should be in the sentence: ").strip().lower

# Using Input To Find The Word And Replace It With There Inputted Word
location = sentence.find(word)
new_sentence = sentence.replace(word,new_word)
print(new_sentence)
print(sentence.find("over"))

# Getting Name And Getting Rid Of Spaces And Recombining Name Into Full Name
first_name = input("What is your first_name: ").strip().title()
last_name = input("What is your last_name: ").strip().title()
first_seperated = first_name.split()
last_seperated = last_name.split()
last_fixed = " ".join(last_seperated)
first_fixed = " ".join(first_seperated)
full_name = first_fixed.title() + " " + last_fixed.tiltle()
print("Hello " + full_name.title())

# Showing What The Sentence Has Checking Is All Is Upper Case isupper, And If It Is All Numbers isnumeric, And If It Is All Characters isalpha
print(full_name.isalpha)
print(full_name.isnumeric)
print(full_name.isupper)

# Printing The Sentence In Different Ways
print(sentence.lower())
print(sentence.upper())
print(sentence.capitalize())
print(sentence.title())


# Formatted string
print(f"Hello {first_fixed.title} {last_fixed} welcome to my program! ")"""

# Findin the asky or numeric value of the letter then adding two to its numeric value to make a new letter
letter = input("Give me a letter: ")
letter = letter[0].lower()
number_value = ord(letter)
number_value += 2
new_letter = chr(number_value)
print(f"Your letter was {letter} now it is {new_letter}")