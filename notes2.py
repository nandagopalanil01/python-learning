#unpacking lists 
person1 = ['Shrawani', 20, 'Researcher', 'India']
#Useing only indexes makes the code long and hard to extend

name1, age, role, country = person1    #variable must match the list values order.
print(country)
print(name1)

#Asterisk
person2 = ['Nandu', 23, 'Data engineer', 'Germany']
name2, *details, country = person2  #if we only want 1st and last item
print(name2)
print(details)
print(country)
#note : only one asterisk (*) is alowed in unpacking

#Skipping Items - Underscore "_"
user = ['Meena', 40, 'Govt', 'Japan']
name, _, _, country = user
print(name)
print(country)

#Combining '*' and '_'
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] #we only need first and least items
first, *_, last = numbers
print(last)
print(first)

