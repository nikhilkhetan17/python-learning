fruits = ['apple' , 'mango', 'banana', 'cherry']

# for e in fruits:
#     print(e)
#     if e == 'mango':
#         break

for ele in fruits:
    if ele == 'mango':
        # break
        continue
    print(ele)


nums = [-10, 20, -30, -40, 50, -60, 70]


for e in nums:
    if e < 0:
        continue
    print(e)


# msg = ''
while True:
    msg = input('Enter your message: ')
    if msg == 'quit':
        break
    else:
        print(msg)







