emptyList = []  # create a list

print(type(emptyList))  # print the type of it list

emptyList.append(1)  # add element to list (adds element to the end of the list)

newList = emptyList  # assign to another list

print(newList)  # print list

newList.insert(0, 2)  # insert is different from append , insert works with index and element

print(newList)  # newList already has 1 , above we inserted element 2 in index 0

# newList.remove(0)  # removes first element in the list whose value equal to 0 , if there is no such element
# ValueError -- Throws error here

# del newList  # it deletes the list

newList.remove(1)  # removes element 1 from list

newList.pop(0)  # remove element with index position , it removes element (which is 2 )

newList = [20, 10, 30, 'Apple', 'Orange']  # create a list with different types

print(newList)

newList[4] = 'Mango'  # change element in the index Orange will be replaced by Mango

print(newList[2])  # prints the element for the index , in index 2 has 30 .

# Usually indexes starts from 0 . [0] = 10 [1] = 20  ......

newList.append(50)  # adds to the last index

print(newList)

newList.pop(-3)  # it removes from list depends on index  [-1] = 50 , [-2] = 'Mango' [-3] = 'Apple' ..... it removes
# element Apple
newList.pop(-2)

print(newList)
print('-----------------------------------------------------------------------------------------------------------')
newList.sort()  # it sort the elements in the list , all the elements should be same type

print(newList)

listWithStrings = ['Orange', 'Apple', 'Mango', 'Pineapple']

print(listWithStrings)  # prints the listWithStrings before sort

listWithStrings.sort()  # it sorts elements alphabetically

print(listWithStrings)  # prints the listWithStrings after sort

listWithStrings.reverse()  # reverse the elements

print(listWithStrings)
print('-----------------------------------------------------------------------------------------------------------')
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.

thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList)

print(thisList[-1])  # return last element in the list

print(thisList[2:5])  # return elements from index 2 to 4 ( index 5 is not included )

print(thisList[:4])  # returns the elements from 0 to 3 ( prints first four elements )

print(thisList[2:])  # returns the elements from index 2 to end

print(thisList[-4:-1])  # return elements index -4 to -1( not included )

print('-----------------------------------------------------------------------------------------------------------')

# looping through the list

for x in thisList:
    print(x)  # prints the elements in the list

print(len(thisList))  # returns the number of elements in the list

if 'apple' in thisList:
    print('True')
else:
    print('False')

copyList = thisList.copy()  # copies elements to copyList List

print(copyList)

print('-----------------------------------------------------------------------------------------------------------')

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

newListOflist1Andlist2 = list1 + list2  # it adds both lists to new list

print(newListOflist1Andlist2)

for i in list1:  # another way to adds lists
    list2.append(i)  # adds elements from list1 to list2

print(list2)

list2.extend(list1)  # adds list1 to end of list2
print(list2)

createList = list((1, 2, 3))  # another way to create list

print(createList)
