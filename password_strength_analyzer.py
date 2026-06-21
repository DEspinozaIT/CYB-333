password = input("Enter a password to analyze: ")

print("\nPassword Analysis")
print("-----------------")
print(f"Length: {len(password)}")

if len(password) >= 15:
    print("Length Requirement: PASS")
else:
    print("Length Requirement: FAIL - Password should be at least 15 characters.")