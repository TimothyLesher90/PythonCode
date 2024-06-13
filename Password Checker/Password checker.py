import re

#List of common passwords
common_passwords=['123456', 'password', '123456789', '12345678', '12345', '1234567',
    '1234567890', 'qwerty', 'abc123', 'password1', '123123']

# Function to check password strength
def is_weak_password(password):
    #check minimum lenght
    if len(password) <8:
        return True, "Password is too short(minimum 8 Characters)."
    
    #check for both letters and numbers
    if not re.search("[a-zA-Z]", password) or not re.search("[0-9]", password):
        return True, "Password must contain both letters and numbers."
    
    #check if password is common
    if password in common_passwords:
        return True, "Password is too common."
    
    return False, "Password is strong."

# Function to check a list of passwords

def check_password_list(password_list):
    for password in password_list:
        is_weak, message =is_weak_password(password)
        print(f"Password: {password} - {message}")

# Example list of passwords to check
passwords_to_check = [
    "123456", "password", "letmein123", "P@ssw0rd", "weakpass", "1234abcd", "Str0ngP@ss"
]

# Main function
def main():
    print("Checking password strength:")
    check_password_list(passwords_to_check)

if __name__ == "__main__":
    main()