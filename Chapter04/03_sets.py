# Sets
colors = {'white', 'blue', 'green', 'white'}
print(colors)

colors.add('purple') # add elements
print('Before deleting set values : ',colors)

colors.remove('blue') # remove elements
colors.discard('abc') # remove elements
print('After deleting set values : ',colors)

# Create empty set
empty_set = set()
empty_set.add(10) # add elements
empty_set.add(20)
empty_set.add(30)

empty_set.remove(10) # add elements

for i in empty_set: # print set elements
    print(i)

print('Is element present in set?: ', 20 in empty_set)

# union, intersection, difference, Symmetric Difference
print('Interview questions')
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b) #union
print(a & b) # intersection
print(a - b) #difference - prints elements from a which are not in b ex:1,2
print(a ^ b) # Symmetric Difference means only uniqe elements returns, ex- 3 is not printed

# Removing Duplicates from List
nums = [1, 2, 2, 3, 3, 4]
unique_nums = set(nums)
print('Unique elements : ',unique_nums)