from urllib import response


print('Gullible')
while True:
    print('to know how to keep a gullible person busy for hours? Y/N')
    response=input('> ')
    if response.lower()=='no' or response.lower()=='n':
        break
    if response.lower()=='yes' or response.lower()=='y':
        continue
    print(f'"{response}" is not a valid yes/no response.')
print('Thank you. Have a nice day!')