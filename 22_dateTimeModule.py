# from datetime import datetime
# print(datetime.now())

import datetime
# print(datetime.datetime.now())

curr = datetime.datetime.now()
print(curr)
print(curr.date())
print(curr.time())

print('-----------------------------------')

# date formatting 2024/06/28
formattedDate = curr.strftime('%Y/%m/%d')
print(formattedDate)

print('-----------------------------------')

# future date
futureDate = curr + datetime.timedelta(days= 10)
print(futureDate)

print('-----------------------------------')

print(f'Date:{curr.day}/{curr.month}/{curr.year} Time:{curr.hour}:{curr.minute}')
