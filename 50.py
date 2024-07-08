def calcmsg1(s1,fname):
    f1=open(fname,"r")
    param1=[]
    param2=[]
    param3=[]
    param4=[]
    for i in range(0,4,1):
        str1=f1.readline().replace("\n","")
        list1=str1.split(",")
        param1.append("Mr.")if list1[0]=="M" else param1.append("Mrs.")
        param2.append(list1[1])
        param3.append(list1[2])
        param4.append(list1[3])
    len1=len(param1)
    for i in range(0,len1,1):
        s2=s1.replace("$1salutation",param1[i]).replace("$2name",param2[i]).replace("$3amount",param3[i]).replace("$4date",param4[i])
        print(s2)
f2=open("template1.txt","r")
s1=f2.readline().replace("\n","")
calcmsg1(s1,"list1.txt")
