# This code generates a Band name for the user
"""
1. Create a greeting for your program.
2. Ask the user for the city that they grew up in and store it in a variable.
3. Ask the user for the name of a pet and store it in a variable.
4. Combine the name of their city and pet and show them their band name.
5. Make sure the input cursor shows on a new line:
"""
print("Welcome to the Band Name Generator.")
name_of_city = input("Which city did you grow up in?\n")
pet_name = input("What is the name of a pet?\n")
print("Your Band name could be " + name_of_city + " " + pet_name)