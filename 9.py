def table1(start,end):
    for j in range(start,end+1,1):
        for i in range(1,11,1):
            print(j,i,j*i)
        print()    
n1=int(input("Enter starting number:"))
n2=int(input("Enter ending number:"))
table1(n1,n2)
