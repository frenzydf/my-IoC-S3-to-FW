def escribir(valor):
    f = open('cloud/actual.txt', "a")
    f.write('\n')
    f.write(valor)
    print(valor ,"Added to a IoC")
    f.close()


with open('src/ioc.txt', 'r') as f_ioc:
    for l_ioc, line_ioc in enumerate(f_ioc):
        my_ioc = line_ioc.strip()
        exist = False
        with open('cloud/actual.txt', 'r') as f_actual:
            for l_actual, line_actual in enumerate(f_actual):
                my_actual = line_actual.strip()
                if my_ioc == my_actual:
                    print(my_ioc ,"already exist")
                    exist = True
                    break
            if exist == False: 
                escribir(my_ioc)
    f_actual.close()
f_ioc.close()
