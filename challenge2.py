# Validate the quality and correctness of Email values

email = "shrawaiicarly123@gmail.com"
#clean the string
email = email.strip()
#must not be empty
if email == "":
    print("Email Cannot be empty")

#must contain '.' and '@'
elif not("." in email and "@" in email):
    print("must contain '.' and '@'")

#must contain exactly one '@' symbol
elif email.count("@") != 1:
    print(" Email must contain exactly one @")

#Must end with .com, .org or .net
elif not email.endswith((".com", ".org", ".net")):
    print("Email must end with .com, .org or .net")

#Must not be longer than 250 charters
elif len(email) >= 250:
    print( "Email must not be longer than 250 characters")

#Must start and end with a letter or digit
elif not (email[0].isalnum() and email[1].isalnum()):
    print("Must start and end with a letter or digit")
    

else:
    print("Email is valid")