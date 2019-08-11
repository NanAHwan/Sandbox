"""Nan A Hwan
"""
user_name = input("Please enter your name: ")
if user_name != "":
    print(user_name[1:len(user_name): 2])
else:
    print("Must not be empty.")
    user_name = input("Please enter your name: ")
