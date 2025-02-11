import random

def to_lowercase_ascii(text):
    """
    Converts a string to lowercase using ASCII values.
    """
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':  # Check if character is uppercase
            result += chr(ord(char) + 32)  # Add 32 to ASCII value to convert to lowercase
        else:
            result += char  # Keep non-uppercase characters as is
    return result

# Example usage
string = "HeLlO WoRlD!"
string = to_lowercase_ascii(string)
print(string)  # Output: "hello world!" 

hii =   input("Hai").lower()