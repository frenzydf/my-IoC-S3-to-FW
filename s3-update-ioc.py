with open(r'src/ioc.txt', 'r') as f_ioc:
    for l_ioc, line_ioc in enumerate(f_ioc):
        my_ioc = line_ioc.strip()
        with open(r'cloud/actual.txt', 'r') as f_actual:
            for l_actual, line_actual in enumerate(f_actual):
                my_actual = line_actual.strip()
                if my_ioc == my_actual:
                    print(my_ioc ,"already exist")
                    break