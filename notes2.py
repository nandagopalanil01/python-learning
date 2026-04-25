#combining lists
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
comb = letters + numbers
print(comb)
# print(letters * 2)  #makes multiple copies of the same list

comb = [letters, numbers]  
print(comb)

numbers.extend(letters)  #extend() doesn't create a new list, it expands the original copy
print(letters)
print(numbers)

#zip()
comb =list(zip(letters, numbers)) #python stops at the shortest list
print(comb)  #you can also pair them with string values. eg. zip(letters, numbers, "hi")

#task: pair customers with their IDs(rebuild the relationship)
id = [101, 102, 103]
names = ['ali', 'shrav', 'nan']
combine = list(zip(id, names))   #make sure the order of the list is correct
print(combine)

