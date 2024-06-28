# for i in 10, 20, 30, 40, 50:
#     print(i)


userName = ['nikhil', 'rahul', 'jeevesh']

for ele in userName:
    print(ele)

# for x in "banana":
#   print(x)


dictionary = {
    'FullName': 'Nikhil Khetan',
     'Age': 25,
     'City': 'raipur'
}

for key, val in dictionary.items():
    print(f'key: {key} and value: {val}')


for val in dictionary.values(): # same for keys -> dictionary.keys()
    print(f'Value is: {val}')

# print numbers from 1 to 20:

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
    
# for i in range(1 , 21):
#     print(i)
        
        
'''
for ele in range(1, 16):
    if ele % 3 == 0 and ele % 5 == 0:
        print(f'{ele} FIZZBUZZ')
    elif ele % 5 == 0:
        print(f'{ele} BUZZ')
    elif ele % 3 == 0:
        print(f'{ele} FIZZ')
    else:
        print(ele)
'''
