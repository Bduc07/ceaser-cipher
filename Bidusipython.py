
import os

def welcome():
    """Prints a welcome message to the user."""
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text using Caesar Cipher.")

def enter_message():
    """Asks the user for a message to encrypt or decrypt."""
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode not in ['e', 'd']:
            print("Invalid Mode")
            continue

        message = input(
        f"What message would you like to {'encrypt' if mode == 'e' else 'decrypt'}: ").upper()

        while True:
            try:
                shift = int(input("What is the shift number: "))
                break
            except ValueError:
                print("Invalid Shift")

        return mode, message, shift

def encrypt(message, shift):
    """Encrypts a message using Caesar Cipher."""
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def decrypt(message, shift):
    """Decrypts a message using Caesar Cipher."""
    return encrypt(message, -shift)

def process_file(filename, mode):
    """Encrypts or decrypts a file using Caesar Cipher."""
    while True:
        try:
            shift = int(input("What is the shift number: "))
            break
        except ValueError:
            print("Invalid Shift. Please enter a valid integer.")

    result = []
    with open(filename, 'r', encoding='utf-8') as file:
        for data in file:
            result.append(encrypt(data, shift) if mode == 'e' else decrypt(data, shift))
        # Close the file after processing all the data
    return result

def is_file(name):
    """Checks if a file exists."""
    return os.path.exists(name)

def write_message(messages):
    """Writes the encrypted or decrypted message to a file."""
    with open("result.txt", "w", encoding='utf-8') as file:
        for message in messages:
            file.write(message + "\n")

def message_or_file():
    """Asks the user if they want to encrypt or decrypt a message or file."""
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()

        if mode not in ['e', 'd']:
            print("Invalid Mode")
            continue

        while True:
            source = input("Would you like to read from a file (f) or the console (c)? ").lower()
            if source == 'f':
                while True:
                    filename = input("Enter a filename: ")
                    if is_file(filename):
                        return mode, filename, None

                    print("Invalid Filename")
                    continue

            else:
                message = input(
                    f"What message would you like to {'encrypt' if mode == 'e' else 'decrypt'}: "
                    ).upper()
                return mode, None, message

def main():
    """Main program function."""
    welcome()

    while True:
        mode, filename, message = message_or_file()
        if filename:
            messages = process_file(filename, mode)
            write_message(messages)
            print("Output written to results.txt")
        else:
            while True:
                try:
                    shift = int(input("What is the shift number: "))
                    break
                except ValueError:
                    print("Invalid Shift")
            print(encrypt(message, shift) if mode == 'e' else decrypt(message, shift))

        another = input("Would you like to encrypt or decrypt another message (y/n): ").lower()
        if another == 'y':
            continue
        print("Thanks for using the program, goodbye!")
        break

if __name__ == "__main__":
    main()
