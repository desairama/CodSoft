import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            password = generate_password(length)
            print("Generated Password:", password)
            break
        except ValueError as ve:
            print("Error:", ve)
            print("Please enter a valid length.")

if __name__ == "__main__":
    main()
