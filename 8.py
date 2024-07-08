def table1(start,end):
    for j in range(start,end+1,1):
        for i in range(1,11,1):
            print(j,i,j*i)
        print()    
table1(3,8)
table1(50,54)
table1(2005,2007)
