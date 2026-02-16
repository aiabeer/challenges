def encode(plain_text):
    # First, transform the text using Atbash cipher
    transformed = ""
    for char in plain_text.lower():
        if char.isalpha():
            # Atbash transformation: a(97) ↔ z(122)
            # 122 + 97 = 219, so 219 - ord(char) gives the opposite letter
            transformed += chr(219 - ord(char))
        elif char.isdigit():
            transformed += char
        # Skip spaces and punctuation
    
    # Now group into chunks of 5 characters
    grouped = []
    for i in range(0, len(transformed), 5):
        grouped.append(transformed[i:i+5])
    
    return " ".join(grouped)


def decode(cipher_text):
    # Remove spaces and decode
    plain_text = ""
    # First remove all spaces from the cipher text
    cipher_text_no_spaces = cipher_text.replace(" ", "")
    
    for char in cipher_text_no_spaces:
        if char.isalpha():
            # Same transformation works both ways
            plain_text += chr(219 - ord(char))
        elif char.isdigit():
            plain_text += char
    
    return plain_text