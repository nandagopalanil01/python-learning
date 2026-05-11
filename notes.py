#Lambda functions
#tax = lambda price: price * 1.2

multiple = lambda x: x * 2
print(multiple(5))

add = lambda x,y : x + y
print(add(1,2))

check = lambda i : i in "python"
print(check('n'))
print(check('z'))

#lambda + map
#task: prices are stored as messy strings and need cleaning to floats
prices = ['$12.50', '$9.99', '$100.00']   #formula= float(p.replace('$', ''))
print(list(map(lambda p: float(p.replace('$', '')), prices)))


#lambda + Filter
#task: Remove all prices lower than 100
prices = [120, 30, 300, 80]
print(list(filter(lambda p: p>100, prices)))

#task: Keep only students with score higher than 70
students = [
    ['Maria', 85],
    ['Kumar', 90],
    ['Max', 60]
]
print(list(filter(lambda row: row[1] > 70, students))) 

#task: keep only stuendts with names starting with 'M'
students = [
    ['Maria', 85],
    ['Kumar', 90],
    ['Max', 60]
]
print(list(filter(lambda row: row[0].startswith('M'), students)))