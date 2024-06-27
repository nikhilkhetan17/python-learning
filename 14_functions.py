def myFun():
    print('function called')

myFun()


def greetUser(name, age = None,): # default value
    print(f'Hello {name} your age is {age}')

greetUser('nikhil', 25)
greetUser('rahul')


# Dynamic function arguments (*, **)

def printUser(name, *hobbies):
    # print(hobbies) # * is tuple
    print(f'Hello {name} your hobbies:')
    for ele in hobbies:
        print(f'- {ele}')

printUser('Nikhil', 'Swimming', 'Dancing')
printUser('Rahul', 'Reading', 'Writing')


def userDetails(name, **userInfo): # ** is dictionary
    print(f'Hello {name}')
    # print(userInfo)
    for key, val in userInfo.items():
        print(f'- {key}: {val}')

userDetails('Nikhil Khetan', age=25, city='Raipur')

# ##########################################################

def sum(num1, num2):
    return num1 + num2

result = sum(10, 20)
print(f'Sum of two no. is {result}')