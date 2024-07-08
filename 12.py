def table2(start,end):
    for j in range(start,end+1,1):
        for i in range(1,11,1):
            str2=str(j)+"*"+str(i)+"="+str(j*i)
            print(str2)
            f2.write(str2)
            f2.write("\n")
        print()
        f2.write("\n")
f1=open("in2.txt","r")
f2=open("out1.txt","w")
str1=f1.readline().replace("\n","")
list1=str1.split(",")
n1=int(list1[0])
n2=int(list1[1])
table2(n1,n2)
f2.close()
