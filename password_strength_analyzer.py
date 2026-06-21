password = input("Enter a password to analyze: ")

print("\nPassword Analysis")
print("-----------------")
print(f"Length: {len(password)}")

if len(password) >= 15:
    print("Length Requirement: PASS")
else:
    print("Length Requirement: FAIL - Password should be at least 15 characters.")

has_upper = any(char.isupper() for char in password)

if has_upper:
    print("Uppercase Requirement: PASS")
else:
    print("Uppercase Requirement: FAIL - Add at least one uppercase letter.")

has_lower = any(char.islower() for char in password)

if has_lower:
    print("Lowercase Requirement: PASS")
else:
    print("Lowercase Requirement: FAIL – Add at least one lowercase letter.")