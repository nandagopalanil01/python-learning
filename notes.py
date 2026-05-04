#ITERATORS

#task: we use iteration to transform data.
letters = ['a', 'b', 'c']
new_list = []
for l in letters:
    new_list.append(l.upper())
    print(new_list)

#enumerate reversed zip
letters = ['a', 'b', 'c']
for index, value in enumerate(letters):
    print(index, value)

#reversed
letters = ['a', 'b', 'c']
for l in reversed (letters):
    print(l)

#zip()
letters = ['a', 'b', 'c']
numbers = [1, 2 , 3]
for l, n in zip(letters, numbers):
    print(l,n)

#map
letters = ['a', 'b', 'c']
#task: make every ketter uppercase
print(list(map(str.upper, letters)))

#task: convert the list items to integer numbers
numbers = ['1', '2', '3']
print(list(map(int, numbers)))

#task: clean up the list by removing all unwanted spaces
names = [' Maria  ', 'John ', '  Kumar ']
print(list(map(str.strip, names)))


#filters

#task: clean up the list by removing unwanted data.
letters = ['a', '', 'b', None, 'c', False]
print(list(filter(None, letters)))

#task: keep only letters
items = ['sql', '123', 'python', '42']
print(list(filter(str.isalpha, items)))
