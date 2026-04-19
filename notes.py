#Nested loops - loop inside another loop
for x in (1,2,3):        #outer loop
    for y in(1,2):       #inner loop
        print(x,y)
##################
for x in range(3):
    for y in range(2):
        for z in range(3):
            print(f"({x}, {y}, {z})")
##################
#crossing data
colors = ['red', 'green', 'yellow']
sizes = ['L', 'M', 'S']
for color in colors:
    for size in sizes:
        print(f'{color} - Size: {size}')

#Navigate Hierarchy
years = [2026, 2027]
months = ['Jan', 'Feb']
days = range(1, 29)

for year in years:
    for month in months:
        for day in days:
            print(f'report_{year}_{month}_{day}.csv')

#Select count(*) from customers where ID is null
tables = ['customers', 'orders', 'products', 'prices']
colums = ['id', 'create_date']
for t in tables:
    for c in colums:
        print(f'SELECT count(*) FROM {t} WHERE {c} IS NULL;')


     ### WHILE LOOP()
# 1- While condition
i = 1
while i < 4:
    print(i)
    i += 1
#Task = Build a counter from 1-10
count = 1  #intialization
while count <= 10:  #condition
    print(count)
    count += 2  #update: this step is really important otherwise the code will keep running for ever

 #task : write a program that keeps asking "Do you agree?" until the user types "yes"
answer = ""
while answer != "yes":
    answer = input("Do you agree?(yes/no): ")
print("Thank You")
