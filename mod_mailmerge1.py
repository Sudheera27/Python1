def calcmsg3(fname1,fname2,fname3):
    f1=open(fname1,"r")
    f2=open(fname2,"r")
    f3=open(fname3,"w")
    s1=f2.readline().replace("\n","")
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
        f3.write(s2)
        f3.write("\n")
