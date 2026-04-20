#while true 
while True:
    answer = input("Do you consent? (yes/no): ")
    if answer == "yes":
        break
print("Thank You")

#Challenge -1.allow up to 3 attempts
#           2.if the user types yes print something
#           3.Otherwise print"3 strikes you are out!"
attempts = 0
while attempts < 3:
    answer = input("Do you agree the Messi is the GOAT? (yes/no)")
    if answer == "yes":
        print("Glad we are on the same page!")
        break
    attempts += 1
else:
    print("3 strikes and you are out")
print("Thank you!")
     