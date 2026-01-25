# Exception handling - try, except, else & finally
try:
    # num =  10 / 0
    print('Running try block...')
    # int('abcd')
except (ZeroDivisionError, ValueError) as e:
    print('Error details : ', e)
else:
    print('There are no exceptions in the try block')
# except ValueError:
#     print('Invalid number')
finally:
    print('Closing all the connection..')