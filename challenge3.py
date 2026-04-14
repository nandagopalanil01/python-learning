#1Check if the user's name. is not empty and the age is greater than or equal to 18
user_name = "nandu@619"
age = 25
if user_name != "" and age >= 18:
    print("Valid user")
else:
    print("Invalid user")

# Check if the passord is at least 8 characters long and doesn't contain spaces.
password = "batm an619"
if len(password) >= 8 and " "not in password:
    print("Valid Password")
else:
    print("Invalid Password")

#3. Check if a user's email is not empty, contains '@', and ends with '.com'.
email = "nanduanil123@gamil.com"
if email != "" and "@" in email and email.endswith(".com"):
    print("Valid Email")
else:
    print("Invalid Email")

#Check if a username is a string, is not a None, and is longer than 5 characters.
username = "Batman#456"
if isinstance(username, str) and username is not None and len(username) > 5:
    print("Strong Username")
else:
    print("Week Username")

#Check if the user is either an admin or a moderator, and either they're not banned or
#  they've verified their email.
role = "Admin"
is_banned = False
is_varified = True

if role == ("Admin" or role == "Moderator") and (not is_banned or is_varified):
    print("Access granted")
else:
    print("Access denied")

