def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age < 18:
        raise ValueError("You must be 18 or older")
    else:
        print("Welcome! You are eligible.")

try:
    check_age(15)
except ValueError as e:
    print("Error:", e)


