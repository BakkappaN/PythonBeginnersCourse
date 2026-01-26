# List
numbers = [10, 20, 30, 40, 50]
colors = ['white', 'red', 'blue']
mixed = [100, 'blue', 10.11, True]

# Append element to list
numbers.append(60)
numbers.append(70)

# Update value
numbers[0] = 1000

# Remove element
numbers.remove(40)

#Check if element is present
print('Is number present : ', 200 in numbers)

# Access list element using index no.
print('Direct access approach 1 : ',numbers[2])
print('Direct access approach 2 : ',numbers[-1])

# Access all list elements using for loop
for item in colors:
    print(item)

# Access all list elements using for loop with index
for i in range(len(numbers)):
    print('Using index : ',numbers[i])