import random

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def caesar_cipher(text: str, shift: int):
    result = ""
    for char in text:
        if char in charset:
            new_index = (charset.index(char) + shift) % len(charset)
            new_char = charset[new_index]
            if random.choice([True, False]):
                new_char = new_char.upper()
            else:
                new_char = new_char.lower()
            result += new_char
        else:
            result += char
    return result

def caesar_decipher(text: str, shift: int):
    result = ""
    for char in text:
        if char.lower() in charset:
            new_index = (charset.index(char.lower()) - shift) % len(charset)
            new_char = charset[new_index]
            if char.isupper():
                new_char = new_char.upper()
            else:
                new_char = new_char.lower()
            result += new_char
        else:
            result += char
    return result


secret_message = "According to all known laws of aviation there is no way a bees hould be able to fly, Its wings are too small to get its fat little body off the ground The bee, of course, flies anyway because bees don't care what humans think is impossible."
number = 3

encrypted_message = caesar_cipher(secret_message, number)
print("Encrypted:", encrypted_message)
print("Decrypted:", secret_message)
