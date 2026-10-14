"""Encrypt or decrypt text with a Caesar cipher."""


def caesar_cipher(text, shift, direction=1):
    """Shift letters by ``shift`` places, preserving case and other characters.

    Use direction=1 to encrypt and direction=-1 to decrypt.
    """
    shift = (shift * direction) % 26
    result = []

    for character in text:
        if "A" <= character <= "Z":
            base = ord("A")
            result.append(chr((ord(character) - base + shift) % 26 + base))
        elif "a" <= character <= "z":
            base = ord("a")
            result.append(chr((ord(character) - base + shift) % 26 + base))
        else:
            # Spaces, punctuation, digits, and symbols are left unchanged.
            result.append(character)

    return "".join(result)


def main():
    print("Caesar Cipher")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    choice = input("Enter your choice (1 or 2): ").strip()
    if choice not in ("1", "2"):
        print("Invalid choice. Please enter 1 or 2.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value: "))
    except ValueError:
        print("The shift must be a whole number.")
        return

    encrypting = choice == "1"
    direction = 1 if encrypting else -1
    action = "Encrypted" if encrypting else "Decrypted"
    print(f"{action} message: {caesar_cipher(message, shift, direction)}")


if __name__ == "__main__":
    main()
