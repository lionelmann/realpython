"""Script should determine the first letter of the user's input \
convert it to uppercase and display it back"""

password = input("Tell me your password")

response = password.upper()

if response == "":
    print("Nothing here")
else:
    print(response[0])
