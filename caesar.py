import string
alphabet = string.ascii_lowercase
def alphabet_position(char):
    newchar = str.lower(char)
    CharIndex = alphabet.index(newchar)
    return CharIndex
def rotate_character(char, rot):
    if char.isalpha() == True:
        letterIndex = alphabet_position(char)
        rotatedIndex = letterIndex + rot
        if rotatedIndex < 26:
            encrypted = alphabet[rotatedIndex]
        else:
            encrypted = alphabet[rotatedIndex % 26]
        if char.isupper() == True:
            return encrypted.upper()
        else:
            return encrypted
    return char


def encrypt(text, rot):
    encryption = ''
    for char in text:
        if char == ' ':
            encryption = encryption + ' '
        else:
            encryption = encryption + rotate_character(char, rot)
    return encryption
