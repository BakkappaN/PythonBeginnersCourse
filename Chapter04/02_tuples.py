mixed = (10, 'green', 12.12, 10, True)

# Access tuple element using index no.
print('Direct access approach 1 : ',mixed[0])
print('Direct access approach 2 : ',mixed[-1])

# Print tuples elements
for item in mixed:
    print(item)

# Tuples methods
print('Count : ',mixed.count(10))
print('Index : ',mixed.count('green'))

# Packing & unPacking
person = ('Jhon', 30, 'QA')
name, age, role = person
print(name)
print(age)
print(role)