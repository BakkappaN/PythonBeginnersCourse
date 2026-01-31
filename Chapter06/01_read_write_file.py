# with open function
with open("data.txt","r+") as file:
    print('Before writing the data')
    print(file.read()) # read the file

    file.write("\nHello!, Testers Talk") # write into the file

    file.seek(0) # position back starting of the file

    print('After writing the data')
    print(file.read()) # read the file