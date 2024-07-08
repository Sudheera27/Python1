def table3(start,end):
    info1=""
    for j in range(start,end+1,1):
        for i in range(1,11,1):
            str2=str(j)+"*"+str(i)+"="+str(j*i)
            info1=info1+str2+"\n"
        info1=info1+"\n"
    return info1
f1=open("in2.txt","r")
f2=open("out1.txt","w")
str1=f1.readline().replace("\n","")
list1=str1.split(",")
n1=int(list1[0])
n2=int(list1[1])
result=table3(n1,n2)
f2.write(result)
print(result)
f2.close()
