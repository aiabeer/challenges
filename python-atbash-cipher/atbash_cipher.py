def encode(plain_text):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            cipher_char = chr(122 - (ord(char.lower()) - 97))
            cipher_text += cipher_char
        elif char.isdigit():
            cipher_text += char
        elif char.isspace():
            cipher_text += " "
    return cipher_text

def decode(cipher_text):
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():
            plain_char = chr(122 - (ord(char.lower()) - 97))
            plain_text += plain_char
        elif char.isdigit():
            plain_text += char
        elif char.isspace():
            plain_text += " "
    return plain_text