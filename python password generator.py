import string
import random

def generate_password(length):
    # Define the possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))

    return password

def get_user_input():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 8:
                print("The password length should be at least 8 characters.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    length = get_user_input()
    password = generate_password(length)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
    