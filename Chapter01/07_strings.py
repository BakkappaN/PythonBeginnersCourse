
str1 = '  Hi!, Welcome to Testers Talk  '
str2 = "Hello!, Welcome to Testers Talk"
str3 = 'testers talk'
print(str1)
print(str2)

print('Strip : ', str1.strip())
print('Length : ', len(str2))
print('Starts-with : ', str2.startswith('123Hello'))
print('Ends-with : ', str2.endswith('123Talk'))

print('Title: ', str2.title())
print('Lowercase : ', str2.lower())
print('Uppercase : ', str2.upper())
print('Capitalize : ', str3.capitalize())

print('Index : ', str2.index('l'))
print('Replace : ', str2.replace('Hello','Hey'))
print('Split :', str2.split(" "))
print('Find :', str2.find('Welcome'))

print('==================')
print('Is digit : ', "1234abc".isdigit())
print('Is alpha : ', "abc123".isalpha())
print('Is alpha numeric : ', "#%%^^".isalnum())

str4 = 'Welcome to Testers Talk'
print('Starting & Ending index : ', str4[0:7])
print('Starting index : ', str4[8:])
print('Ending index : ', str4[:2])
print('Full string : ', str4[:])

print('Negative starting index : ', str4[-2:])
print('Negative ending index : ', str4[:-2])
