import random
import string

def generate_password(length, require_uppercase=True, require_digits=True, require_special=True):
    # Initialize the character set to use
    character_set = string.ascii_lowercase  # Start with lowercase letters

    # Add uppercase letters, digits, and special characters based on user's choice
    if require_uppercase:
        character_set += string.ascii_uppercase
    if require_digits:
        character_set += string.digits
    if require_special:
        character_set += string.punctuation

    password = ''.join(random.choice(character_set) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the desired password length: "))
    require_uppercase = input("Require uppercase letters? (y/n): ").lower() == 'y'
    require_digits = input("Require digits? (y/n): ").lower() == 'y'
    require_special = input("Require special characters? (y/n): ").lower() == 'y'

    if password_length < 1:
        print("Invalid password length. Please enter a positive number.")
    else:
        print("\nGenerated Passwords:")
        for _ in range(num_passwords):
            password = generate_password(password_length, require_uppercase, require_digits, require_special)
            print(password)

if __name__ == "__main__":
    main()
