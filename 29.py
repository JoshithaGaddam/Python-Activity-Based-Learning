print("PASSWORD VALIDATION")

password = input("Enter password: ")

if len(password) < 8:
    print("Password must contain at least 8 characters")

elif not any(ch.isupper() for ch in password):
    print("Password must contain an uppercase letter")

elif not any(ch.islower() for ch in password):
    print("Password must contain a lowercase letter")

elif not any(ch.isdigit() for ch in password):
    print("Password must contain a digit")

elif not any(ch in "@#$!" for ch in password):
    print("Password must contain a special character")

elif "123" in password:
    print("Password must not contain 123")

else:
    print("Valid password")