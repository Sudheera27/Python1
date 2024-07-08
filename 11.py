def table1(start,end):
    for j in range(start,end+1,1):
        for i in range(1,11,1):
            print(j,i,j*i)
        print()    
f1=open("in2.txt","r")
str1=f1.readline().replace("\n","")
list1=str1.split(",")
n1=int(list1[0])
n2=int(list1[1])
table1(n1,n2)
