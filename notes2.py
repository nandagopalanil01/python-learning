#Update Items
letters1 = ['a', 'b', 'c', 'd']
letters1[2] = 'e'  #replaces c with e
print(letters1)

matrix1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
#task: update the content of the last list
matrix1[2] = ['x', 'y', 'z']
print(matrix1)
#update the first item of the first row
matrix1[0][0] = '-'  #updates 'a'
matrix1[1][1] = '-'  #updates 'e'
print(matrix1)

#sorting lists
letters2 = ['c', 'a', 'b', 'd']
letters2.sort()  #sorts the list in ascending order
print(letters2)

letters2.sort(reverse = True) #sorts the list in decending order
print(letters2)

matrix2 =  [
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['a', 'b', 'c']
]
matrix2.sort()  #sorts the first item of each inner list
print(matrix2) 
matrix2[1].sort() #sorts only the 1st row
print(matrix2)

#sorting the data without changing the original list
letters3 = ['c', 'a', 'b']
new_list = sorted(letters3)
print("original list:", letters3)
print("sorted list:", new_list)
new_list = sorted(letters3, reverse = True)
print(new_list)

#Reversing list
letters = ['c', 'a', 'b', 'd']
letters.reverse()
print(letters)

new_list = list(reversed(letters)) #reversed() creates an itenary object and not a list 
print("reversed list:", new_list)
print("original:", letters)


#COPYING LISTS

#assignment = 
original = ['a', 'b', 'c']
copylist = original  #both the variables reference the same list in memory,
#so any change to the new copy will also affect tge original list

#shallow copy
original = ['a', 'b', 'c']
copylist = original.copy()  #copy() creates a separate list in memory
copylist.append('z')
print("original:", original)
print("copy:", copylist)
#this wont work for matix because the method .copy() creates a shallow copy

#deep copy
import copy
matrix = [
    ['a', 'b'],
    ['c', 'd'],
]
matrix_copy = copy.deepcopy(matrix)  #copy.deepcopy() creates a true, iindependent copy for all levels
matrix.pop()
matrix_copy[0].append('x')
print('original:', matrix)
print('copy:', matrix_copy)

#there is one more funtion in copy module, copy.copy() which creates a shallow copy just liske the method copy()

#testing : is operator
import copy
original = [
    ['a', 'b'],
    ['c', 'd'],
]
#assignment
copy1 = original
print("same object?-", original is copy1, "\n")

#shallow copy
copy2 = original.copy()
print("same object?-", original is copy2)  #false: each variable is pointing to a different object in the memory (not identical)
print("shared list?", original[0] is copy2[0], '\n')  #true - sharing same list

#deep copy
copy3 = copy.deepcopy(original)
print("same object?-", original is copy3)
print("shared list?", original[0] is copy3[0], '\n') #both are false meaning 