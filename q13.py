a  = input("Enter a password  :")

b = len(a) >= 8

c = False

for character in a:
    if character.isdigit():
        c = True
if b and c:
    print("Strong Password")

else:
    print("Bad Password")