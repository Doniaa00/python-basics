import string

print("welcome to the password strength checker")
while True:
    password = input("enter a password (or type 'quit' to exit): ")
    if password.lower() == "quit":
        print("goodbye")
        break

    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = 0
    if length >= 8:
        score += 1
    if has_lower and has_upper:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    if score <= 1:
        strength = "weak"
    elif score == 2 or score == 3:
        strength = "medium"
    else:
        strength = "strong"

    print(f"your password is {strength}\n")
