import string
import random

def generate_password(length=12):
    if length < 12:
        print("Password length should be at least 12 characters for better security.")
        return None
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    while True:
        try:
            password_length = int(input("Enter the desired password length (at least 12): "))
            if password_length < 12:
                print("Password length should be at least 12 characters.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    password = generate_password(password_length)
    
    if password:
        print(f"Generated password: {password}")
