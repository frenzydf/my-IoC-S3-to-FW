#Save new IoC IP address to a List

mylist = []
with open(r'src/ioc.txt', 'r') as f: #Open your File txt to read and save IoC
    for line in f:
        mylist.append(line.strip())

#Validation 1 search for a duplicated items

with open(r'cloud/actual.txt', 'r') as fp:
    content = fp.read()
for address in mylist:
    if address in content:
        print(address ,'already exist')
    else:
        print(address ,'is a new item')