# for loop

# Iteration1 i=1
# Iteration2 i=2
# Iteration3 i=3
# Iteration4 i=4
# Iteration5 i=5 return false. then exits for loop

# after custom incrementor as 2
# Iteration1 i=1
# Iteration2 i=3
# Iteration3 i=5 return false. then exits for loop
for i in range(1, 5, 2): 
    print(i)

# Nested for loops
# Iteration1 i=1, j=1, 2, 3, 4, 5
# Iteration2 i=2, j=1, 2, 3, 4, 5
for i in range(1, 5): 
    for j in range(1, 5):
        print(i, j)