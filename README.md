# Caesar Cipher Encryption and Decryption

**Repository:** `PRODIGY_CS_01`  
**Internship:** Prodigy InfoTech Cybersecurity Internship - Task 01

## Project Overview

This project is a simple, command-line Python program that encrypts and decrypts messages using the Caesar cipher. It demonstrates how a basic substitution cipher works and introduces core ideas in cryptography.

## Features

- Choose encryption or decryption from a numbered menu.
- Enter a message and an integer shift value.
- Preserve uppercase and lowercase letters.
- Leave spaces, numbers, and punctuation unchanged.
- Wrap letters around the alphabet when a shift passes `Z` or `z`.
- Display a clear message for an invalid menu choice or shift value.

## Technologies Used

- Python 3
- Python standard library only; no external packages are required.

## Explanation of the Caesar Cipher

The Caesar cipher shifts each letter by a fixed number of positions in the alphabet. Encryption shifts letters forward; decryption shifts them backward by the same amount. The program uses modulo 26 arithmetic to wrap around the 26-letter English alphabet. Characters that are not letters are copied unchanged.

For example, with a shift of 3, `Z` becomes `C` during encryption. This cipher is useful for learning, but it is not secure for protecting real information because its small key space makes it easy to break.

## How to Run the Program

1. Install Python 3 if it is not already installed.
2. Open a terminal in the project folder.
3. Run the script:

   ```bash
   python ceasar_cipher.py
   ```

4. Enter `1` to encrypt or `2` to decrypt, then provide the message and shift value when prompted.

> The script currently in this project is named `ceasar_cipher.py` (spelled "ceasar").

## Example Encryption and Decryption

With a shift value of `3`:

| Operation | Input | Result |
| --- | --- | --- |
| Encryption | `Hello, World!` | `Khoor, Zruog!` |
| Decryption | `Khoor, Zruog!` | `Hello, World!` |

The spaces, comma, and exclamation mark remain unchanged.

## Learning Outcomes

- Understand how a shift cipher maps letters to other letters.
- Use modular arithmetic to wrap around a fixed range.
- Apply the same transformation in opposite directions for encryption and decryption.
- Handle user input and preserve characters outside the alphabet.
- Recognize why a simple classical cipher should not be used to secure sensitive data.
