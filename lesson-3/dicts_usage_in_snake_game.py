# An example of a dict that resemebles the use of the KEY_COLOUR_MAP in the snake game

ALPHABET_VOWELS = {
    "A": "Alpha",
    "E": "Echo",
    "I": "India",
    "O": "Oscar",
    "U": "Uniform"
}

letter = input("Enter a letter: ").upper()  # Get user input and convert to uppercase
if letter in ALPHABET_VOWELS:
    print(f"The value for key {letter} is {ALPHABET_VOWELS[letter]}")
else:
    print(f"{letter} is not a valid vowel in the vowels dictionary.")
