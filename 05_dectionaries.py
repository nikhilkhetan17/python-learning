marks = {
    'science': 80,
    'maths': 50,
    'name': 'Nikhil Khetan',
    'isMajor': True,
    'colors': ["red", "white", "blue"]
}


print(marks)
print(marks['name'])
# print(len(marks))  # dictionary length
print(type(marks))
print(marks['colors'][2])

# print('is person major: ' + str(marks['isMajor']))
print(f'is person major: {marks["isMajor"]}')

# .get() returns none if key is not present rather than throwing error.

print(marks.get('colors'))
print(marks.get('hindi')) # None


# updating value of a dictionary
marks['maths'] = 60


# Adding item to a dictionary
marks['hindi'] = 60
print(marks.get('hindi'))

# Delete value from a dictionary
del marks['science']
print(marks)





