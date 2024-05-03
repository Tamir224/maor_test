import string

def password_generator():
    flag = True
    while flag:
        password = input('Please enter your password: ')

        # Check length
        if len(password) != 9:
            print("Password length must be exactly 9 characters.")
            continue

        # Check if it starts with 'T'
        if not password.startswith('T'):
            print("Password must start with 'T'.")
            continue

        # Check for digits
        has_digit = any(char.isdigit() for char in password)
        if not has_digit:
            print("Password must contain at least one digit.")
            continue

        # Check for punctuation
        has_punctuation = any(char in string.punctuation for char in password)
        if not has_punctuation:
            print("Password must contain at least one punctuation.")
            continue

        # If all conditions are met, return the password
        return password

# Test the function
accepted_password = password_generator()
print("Password accepted:", accepted_password)

