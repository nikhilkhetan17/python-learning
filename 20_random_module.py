import random, math

# Generate a random float between 0 and 1
randonFloat = random.random()
print(randonFloat)


# randomNum = round(random.random() * 4 + 1, 2) # the second argument is decimal places to round
randomNum = math.floor(random.random() * 4 + 1) # number between 1 to 4
print(randomNum)


# Generate a random integer between 1 to 5
randdomInt = random.randint(1, 5)
print(randdomInt)


fruitList = ['apple', 'mango', 'orange', 'kivi']
print(random.choice(fruitList))

# print(round(random.uniform(3.5, 8.5), 2))


