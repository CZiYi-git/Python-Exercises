# Create a dictionary of contact information for your friends and family
contacts = {
  "Bob": {
    "phone": "87162314",
    "email": "bob@example.com"
  },
  "Sally": {
    "phone": "91231411",
    "email": "sally@example.com"
  },
  "Tommy": {
    "phone": "89287305",
    "email": "tommy@example.com"
  }
}

# Ask the user to enter the name of a contact
contact_name = input("Enter the name of a contact: ")

# Check if the contact is in the dictionary and print their phone number and email if they are
if contact_name in contacts:
  print(f"{contact_name}'s phone number is {contacts[contact_name]['phone']}.") 
  print(f"{contact_name}'s email address is {contacts[contact_name]['email']}.")
else:
  print(f"Sorry, {contact_name} is not in our list of contacts.")

# Hints:
# 1. What key is used to get the phone number?
# 2. What key is used to get the email address?