"""Kyle"""

MIN_LEN = 6

password = input("Enter password: ")
while len(password) < MIN_LEN:
    print("Your password isn't long enough")
    password = input("Enter password: ")

print("*"*len(password))