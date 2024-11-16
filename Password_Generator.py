import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    # Define character pools
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    # Build character pool and ensure at least one character from each selected category
    password = []
    if use_upper:
        password.append(random.choice(upper))
    if use_lower:
        password.append(random.choice(lower))
    if use_digits:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special))
    
    # Create the remaining characters
    character_pool = ''
    if use_upper:
        character_pool += upper
    if use_lower:
        character_pool += lower
    if use_digits:
        character_pool += digits
    if use_special:
        character_pool += special
    
    if not character_pool:
        return "Error: Please select at least one character type!"
    
    # Fill the rest of the password length
    while len(password) < length:
        password.append(random.choice(character_pool))
    
    # Shuffle for randomness and return as a string
    random.shuffle(password)
    return ''.join(password)

def get_yes_no_input(prompt):
    """Prompt the user for a yes/no input and validate it."""
    while True:
        response = input(prompt).strip().lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

# User Input
print("Welcome to the Password Generator!")

# Get and validate password length
while True:
    length_input = input("Enter desired password length (minimum 4): ").strip()
    if not length_input.isnumeric():
        print("Error: Please enter a valid number.")
        continue
    length = int(length_input)
    if length < 4:
        print("Error: Password length must be at least 4 for security.")
    else:
        break

# Get user preferences for character types
use_upper = get_yes_no_input("Include uppercase letters? (y/n): ")
use_lower = get_yes_no_input("Include lowercase letters? (y/n): ")
use_digits = get_yes_no_input("Include digits? (y/n): ")
use_special = get_yes_no_input("Include special characters? (y/n): ")

# Ensure at least one character type is selected
if not (use_upper or use_lower or use_digits or use_special):
    print("Error: At least one character type must be selected!")
else:
    # Generate and display the password
    print("\nYour Generated Password:")
    print(generate_password(length, use_upper, use_lower, use_digits, use_special))


