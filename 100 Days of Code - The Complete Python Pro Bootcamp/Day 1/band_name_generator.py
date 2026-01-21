# This code generates a Band name for the user by:
"""
1. Writing a greeting for the User.
2. Asking the user for the city that they grew up in and storing it in a variable.
3. Asking the user for the name of a pet and storing it in a variable.
4. Combining the name of their city and pet and showing them their band name.
5. Also making sure the input cursor shows on a new line:
"""
print("Welcome to the Band Name Generator.")
name_of_city = input("Which city did you grow up in?\n")
pet_name = input("What is the name of a pet?\n")
print("Your Band name could be " + name_of_city + " " + pet_name)