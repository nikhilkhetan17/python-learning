i = 0
# while True:
while i < 5: 
    nums = int(input('Enter a number: '))
    if nums % 2 == 0:
        print('Number is even')
        i = i + 1
    else:
        print('Number is odd')
        i = i + 1

# ##############################################

# userInput = ""
# while userInput != 'q':
#     userInput = input('Enter a number or q to quit: ')
#     if userInput.isdigit():
#         if int(userInput) % 2==0:
#             print('Even')
#         else:
#             print('Odd')

# ########################################

# count = 1
# while count <= 5:
#     print(count)
#     count+=1

# ####################################### 

# active = True
# while active:
#     msg = input('Enter your message: ')
#     print(msg)
#     if msg == 'exit':
#         active = False

# ########################################

listNum = [1, 29, 24, 55, 29, 34, 12, 29]
while 29 in listNum:
    listNum.remove(29) # remove 29 from all occurences

print(listNum)








