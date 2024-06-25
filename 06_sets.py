# Sets are unordered and it ignores duplicate items

mySet = {'mon', 'tue', 'wed', 'mon'}

print(type(mySet))

mySet.add(5)
mySet.add('thu')
mySet.add(True)
print(mySet) 


# convert Array list to Set
myDays = ['mon', 'tue', 'wed', 'mon', 'wed']
setMyDays = set(myDays)

print(myDays)
print(setMyDays)



