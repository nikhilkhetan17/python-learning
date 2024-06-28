'''
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''


print(10*2)

try:
    print(10/0)
# except:
except ZeroDivisionError:
    print('Division by 0 is not allowed')

try:
    with open('userInf.txt') as file:
        # content = file.read()
        content = file.readlines() # returns a array list
    print(content)
# except FileNotFoundError:
except Exception as e:
    print(f'{e}, {type(e)}')
else:
    for ele in content:
        print(f'Hello: {ele.rstrip()}') #rstrip() -> to remove the whitespace
finally:
    # print('finally will run at any cost')
    print('DB Closed')

print(10-2)
print(10+2)


# As a Python developer you can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the raise keyword.
# x = -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")


# The 'is' keyword is used to test if two variables refer to the same object. 
# Raise a TypeError if x is not an integer:
myName = 'Nikhil'
try:
    if not type(myName) is int:
        raise TypeError('Only integers are allowed')
except Exception as ex:
    print(f'Exception caught: {ex}')

print(10+20)


