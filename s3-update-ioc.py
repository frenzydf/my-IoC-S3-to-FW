#Save new IoC IP address to a List

mylist = []
with open(r'src/ioc.txt', 'r') as f_actual: #Open your File txt to read and save IoC
    for line in f_actual:
        mylist.append(line.strip())

#Validation 1 search for a duplicated items

with open(r'cloud/actual.txt', 'r') as f_ioc:
    for address in mylist:
        for l_ioc, line_ioc in enumerate(f_ioc):
            doc_ioc = line_ioc.strip()
            exist = False
            if address in doc_ioc:
                print(address ,'already exist')
                l_ioc = 0
                exist = True
                break
        if exist == False:
            print(address ,"is a new item")