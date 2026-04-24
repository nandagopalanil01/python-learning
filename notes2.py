#CHANGING LIST

#add items
lists = ['a', 'b', 'c']
lists.append('d')  #Append the new value at the end of the list
print(lists)

letters = ['a', 'b', 'c']
letters.insert(0, 'x')
print(letters)
letters.insert(3, 'y')
print(letters)

#adding new row to the end of the matrix
matrix = [
    ['a', 'b', 'c'],    #row 1
    ['d', 'e', 'f'],    #row2
    ['g', 'h', 'i']    #row3
]
matrix.append(['x', 'y', 'z'])  #adds new row at the end
print(matrix)

matrix.insert(0, ['g', 'g', 'g'])  #adds new row at the start
print(matrix)

matrix[1].append('x') #adds 'x at the end of the second row
print(matrix)

matrix[0].insert(0, 'z') #adds 'z at the start of the first row
print(matrix)


#remove items
letters = ['a', 'b', 'c', 'd']
letters.clear()  #clears everthing
print(letters)

letter = ['a', 'b', 'a']
letter.remove('a') #removes by value(removes only the first match)
print(letter)

removed = letter.pop(1) #removes by position (to remove the last item dont need to specify it's default)
print(letter)
print("Removed item:", removed)

#removing from matix
matrix2 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
matrix2.remove(['a', 'b', 'c'])
matrix2.pop()
#remove 'e' from the matrix
matrix2[0].remove('e')
print(matrix2)


#updating items
