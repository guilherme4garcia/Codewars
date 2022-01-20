# Replace With Alphabet Position

# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.

def alphabet_position(text):
    import string
    tabletext = text.translate(str.maketrans('', '', string.punctuation))
    tabletext = tabletext.replace(' ', '').lower()
    alphabet = string.ascii_lowercase
    letter_position = ''
    for word in tabletext:
        letter_position += str(alphabet.index(word) + 1) + ' '

    return letter_position.strip()