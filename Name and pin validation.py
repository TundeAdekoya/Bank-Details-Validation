import string

# PIN VALIDATION 
def validate_pin(pin):
    is_valid = True

    if len (pin) > 4: 
        print("Pin is too long")
        is_valid = False

    if any(char.isupper() for char in pin):
        print("Pin should not containa a uppercase letter [A-Z]")
        is_valid = False

    if any(char.islower() for char in pin):
        print("Pin should not containa a loweercase letter [a-z]")
        is_valid = False

    if not any(char.isdigit() for char in pin):
        print("Pin should contain numbers")
        is_valid = False

    if any(char in string.punctuation for char in pin):
        print(f"Pin should contain special characters {''.join(string.punctuation)}")
        is_valid = False

    if is_valid:
        return f"{(pin)}"
    else:
        return "Invalid Pin"
        

val_pin = validate_pin("1530")
# print(val_pin)


#NAME VALIDATION
# FIRST NAME VALIDATION 
def validate_first_name(first_name):
    is_valid = True

    if any(char.isdigit() for char in first_name):
        print("First Name should not contain numbers")
        is_valid = False

    if any(char in string.punctuation for char in first_name):
        print(f"First Name should not contain special characters {''.join(string.punctuation)}")
        is_valid = False

    if is_valid:
        return f"{(first_name)}"
    else:
        return "Wrong Input"
        

val_first_name = validate_first_name("Tunde")
# print(val_first_name)

# LAST NAME VALIDATION 
def validate_last_name(last_name):
    is_valid = True

    if any(char.isdigit() for char in last_name):
        print("last Name should not contain numbers")
        is_valid = False

    if any(char in string.punctuation for char in last_name):
        print(f"last Name should not contain special characters {''.join(string.punctuation)}")
        is_valid = False

    if is_valid:
        return f"{(last_name)}"
    else:
        return "Wrong Input"
        

val_last_name = validate_last_name("Adekoya")
# print(val_last_name)
print(f"Welcome {(val_last_name)} {(val_first_name)} your pin is {(val_pin)}")



