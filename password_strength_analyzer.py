password = input("Enter a password to analyze: ")
score = 0

print("\nPassword Analysis")
print("-----------------")
print(f"Length: {len(password)}")

if len(password) >= 15:
    print("Length Requirement: PASS")
    score += 1
else:
    print("Length Requirement: FAIL - Password should be at least 15 characters.")

has_upper = any(char.isupper() for char in password)

if has_upper:
    print("Uppercase Requirement: PASS")
    score += 1
    
else:
    print("Uppercase Requirement: FAIL - Add at least one uppercase letter.")

has_lower = any(char.islower() for char in password)

if has_lower:
    print("Lowercase Requirement: PASS")
    score += 1
else:
    print("Lowercase Requirement: FAIL – Add at least one lowercase letter.")

has_number = any(char.isdigit() for char in password)

if has_number:
    print("Number Requirement: PASS")
    score += 1
else:
    print("Number Requirement: FAIL - Add at least one number.")

special_characters = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

has_special = any(char in special_characters for char in password)

if has_special:
    print("Special Character Requirement: PASS")
    score += 1
else:
    print("Special Character Requirement: FAIL - Add at least one special character.")

print(f"\nTotal Score: {score}/5")

if score <= 1:
    rating = "WEAK"
elif score <= 3:
    rating = "MODERATE"
elif score == 4:
    rating = "STRONG"
else:
    rating = "VERY STRONG"

print(f"Password Strength: {rating}")