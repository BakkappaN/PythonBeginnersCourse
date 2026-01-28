# Dictionary
employee = {
    "name" : "Jhon",
    "age" : 30,
    "salary" : 200000
}

employee["age"] = 40 # update value
employee["role"] = 'QA' # add new key-value

# Access value by key
print('Dictionary value : ', employee.get("name"))
print('Dictionary value : ', employee["age"])

# Print all the keys-values
for key, value in employee.items():
    print(f"Key : {key} & Value : {value}")

print('Keys : ', employee.keys()) # print only keys
print('Values : ', employee.values()) # print only values
print('Keys & Values : ', employee.items()) # print keys-values