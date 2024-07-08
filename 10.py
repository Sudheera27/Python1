def table1(start,end):
    for j in range(start,end+1,1):
        for i in range(1,11,1):
            print(j,i,j*i)
        print()    
f1=open("in1.txt","r")
n1=int(f1.readline())
n2=int(f1.readline())
table1(n1,n2)
