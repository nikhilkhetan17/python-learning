# ordered sequence of different types of values

listName =  ["Nikhil", "Rahul", "Prabhat", "Jeevesh"]

print(listName)
print(listName[0]) # to get the values from array on specific index
print(listName[-1]) # to get the last index value

# Adding item to the end of list
listName.append("Yash")
print(listName)

# delete values from list
listName.remove("Nikhil")
print(listName)

# Modify the value of a list
listName[0] = "Rahul Pal"
print(listName)

# Adding item to a list at the specific index
listName.insert(2, "Harshit")
print(listName)

# Delete values from a list using index number
del listName[2]
print(listName)

# length of a list
print(len(listName))


newArr = ['b', 'a', 'd', 'c'] # modifies the original array 

# Sorting of array 
newArr.sort() #sorts in ascending order
print(newArr)

newArr.sort(reverse=True) # sorts in descending order
print(newArr)

newArr2 = ['bb', 'aa', 'dd', 'cc']
newArr2.reverse() 
print(newArr2)

# popping the item in the list
newArr3 = [11, 22, 33, 44, 55]
removedValue = newArr3.pop() # By default removes the last element from the array
print(newArr3)
print(removedValue)

newArr3.pop(0) # give the index number to remove specific element
print(newArr3)

# Slicing of a list 
arr = ['one', 'two', 'three', 'four', 'five']

print(arr[:2]) # Getting the first two elements (arr[0:2])

print(arr[2:]) # Getting all elements starting from index 2 

print(arr[2:4]) # getting middle 2 items

print(arr[-2:]) # getting last 2 items form the list

# Numeric list (getting min, max and sum)
numeric = [10, 20, 30, 40, 50, 60]

print(min(numeric))
print(max(numeric))
print(sum(numeric))




































































