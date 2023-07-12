import random
import string


def generate_random_text(length):
    """Generate a random string of characters of the specified length"""
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = length))


def write_password_to_file(password):
    with open("Generated_passwords.txt", "a") as file:
        file.write(password + "\n")


# Example usage
password = generate_random_text(10)  # generates a random string of 10 characters
write_password_to_file(password)
print(password)