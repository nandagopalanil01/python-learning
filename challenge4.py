#Validate the quality and correctness of the Passwords
email = input("Enter your email")
password = input("Enter your password")


#>must not be empty
if password == "":
    print("password should not be empty")
    
#>must be at least 8 characters
elif len(password) < 8:
    print("password must be at least 8 characters")

#>must include at least one Upppercase
elif not any(c.isupper()for c in password):
    print("must contain atleast one uppercase letter")

#>must include at least one lowercase
elif not any(c.islower() for c in password ):
    print("Password must include at least one lowercase letter")

#>must not be same as email address 
elif password == email:
    print("Password should not be the same as email")

#>must not cantain any spaces
elif " " in password:
    print("Password must not contain any spaces")

#>must start and end with letters or digits
elif not (password[0].isalnum() and password[-1].isalnum()):
    print("Password must start with lettter or space")

else:
    print("Valid password")