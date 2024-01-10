# Vigenere Cipher Package

This Python package provides an implementation of the Vigenere cipher, a method of encrypting text by using a simple form of polyalphabetic substitution.

## Features

- `vigencrypt`: Encrypts a message using the Vigenere cipher.
- `vigdecrypt`: Decrypts a message encrypted with the Vigenere cipher.

## Installation

You can install this package by downloading the `.whl` file and running:

```bash
pip install path/to/vigenere-0.0.1-py3-none-any.whl
```
Note, change `path/to/` to the actual location of the `.whl` on user's computer.

Or, if you have the source code, navigate to the root directory of this package and run:
```bash
pip install .
```
## Usage
Import the vigencrypt and vigdecrypt functions from the package and use them as follows:
```
from vigenere import vigencrypt, vigdecrypt

# Example usage
encrypted_message = vigencrypt("Hello, World!", "KEY")
decrypted_message = vigdecrypt(encrypted_message, "KEY")

print("Encrypted:", encrypted_message)
print("Decrypted:", decrypted_message)
```

## Contributing
Contributions to this package are welcome. Please ensure to write tests for new features and fix any issues you encounter.

## License
This project is licensed under the MIT License - see the LICENSE file for details.