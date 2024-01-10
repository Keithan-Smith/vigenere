def vigencrypt(message, key):
    """
    Encrypts a message using the Vigenere cipher.

    Args:
        message (str): The message to be encrypted. Should contain only alphabetic characters.
        key (str): The encryption key. Should contain only alphabetic characters.

    Returns:
        str: The encrypted message.

    Raises:
        ValueError: If either message or key is empty, not a string, or contains non-alphabetic characters.
    """
    if not isinstance(message, str) or not isinstance(key, str):
        raise ValueError("Both message and key must be strings.")

    if not key.isalpha():
        raise ValueError("Key must contain only alphabetic characters.")

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Define the alphabet
    key = key.upper()
    message = message.upper()
    encrypted_message = ""
    key_index = 0

    for char in message:
        if char in alphabet:
            shift = alphabet.index(key[key_index])
            encrypted_char = alphabet[(alphabet.index(char) + shift) % 26]
            # Maintain the case of the original character
            encrypted_message += encrypted_char.lower() if char.islower() else encrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            # If it is not in alphabet we should return it exactly
            encrypted_message += char

    return encrypted_message


def vigdecrypt(message, key):
    """
    Decrypts a message encrypted with the Vigenere cipher.

    Args:
        message (str): The message to be decrypted. Can contain non-alphabetic characters.
        key (str): The decryption key. Should contain only alphabetic characters.

    Returns:
        str: The decrypted message, maintaining the case and non-alphabetic characters.

    Raises:
        ValueError: If either message or key is empty, not a string, or if key contains non-alphabetic characters.
    """
    if not isinstance(message, str) or not isinstance(key, str):
        raise ValueError("Both message and key must be strings.")

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = ''.join(filter(str.isalpha, key.upper()))  # Remove non-alphabetic characters from key; exists in country keys
    decrypted_message = ""
    key_index = 0

    if not key:
        raise ValueError("Key must contain at least one alphabetic character.")

    for char in message:
        if char.upper() in alphabet:
            shift = alphabet.index(key[key_index])
            decrypted_char = alphabet[(alphabet.index(char.upper()) - shift) % 26]
            # Maintain the case of the original character
            decrypted_message += decrypted_char.lower() if char.islower() else decrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_message += char

    return decrypted_message
