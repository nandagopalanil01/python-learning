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
copylist = original.copy