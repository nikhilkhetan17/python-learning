days = ('mon', 'tue', 'wed', 'thu', 'thu')

print(type(days))
print(days)

print(days[0])
print(days[0:2])

# days[0] = "monday"  #TypeError: 'tuple' object does not support item assignment
# print(days)


print(days.count('thu')) # count the number of occurence of a value
print(days.index('thu')) # returns the first index of value


days = (10, 20, 100) # we can reassign
# print(days)



