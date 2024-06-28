import random

while True:
    print(f'Number is: {random.randint(1, 6)}')
    userInput = input("Do you want to cotinue? y/n: ")
    if userInput == 'n':
        break
    # if userInput == 'y':
    #     continue

    