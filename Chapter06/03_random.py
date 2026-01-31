# Import random module
import random

# Generate random floating point between 0 & 1, random integer
print('Floatin point 0 to 1 : ', random.random())
print('Random integer : ',random.randint(1,100))

# Pick random value from the list
colors = ["red", "blue", "green", "white"]
print('Random color : ', random.choice(colors))

# Shuffle
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print('Shuffle list : ', nums)