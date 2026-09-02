import re
class InvalidPhoneNumberError(Exception):pass

def register_contact(phonebook, name, phone_input):
    try:
        if len(name) == 0 or re.search(r"[0-9]+",name):
            raise ValueError

    except ValueError:
        raise ValueError("Contact name must be a non-empty alphabetic string.")
    
    try:
        phone_string = str(phone_input)
        phone_input = int(phone_input)
        phonebook[name] = phone_string
        return phonebook
    except ValueError:
        raise InvalidPhoneNumberError("Phone number must contain digits only.")

contacts = {}

# 1. Valid Input
contacts = register_contact(contacts, "Alice", "0987654321")
print(contacts)
# Result: {"Alice": "0987654321"}

# 2. Invalid Phone Number (Raises InvalidPhoneNumberError)
try:
    contacts = register_contact(contacts, "Bob", "123-456-789")
except InvalidPhoneNumberError as e:
    print(e)  # Output: Phone number must contain digits only.

# 3. Invalid Name (Raises ValueError)
try:
    contacts = register_contact(contacts, "Bob123", "9876543210")
except ValueError as e:
    print(e)  # Output: Contact name must be a non-empty alphabetic string.
