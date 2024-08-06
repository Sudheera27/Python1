def getyears(fname):  
    f1=open(fname,"r")
    years1=[]
    list1=f1.readlines()

    for i in range(1,21000,1):
        list2=list1[i].split(",")
        year1=list2[0][0:4]
        years1.append(year1)
    set1=set(years1)
    years2=list(set1)
    years2.sort()
    return years2

def createfiles(list1):
    len1=len(list1)
    fname1="olympics2_"
    fname3=".csv"
    list2=[]
    for i in range (0,len1,1):
        fname=fname1+list1[i]+fname3
        list2.append(fname)
        f1=open(fname,"w")
        f1.write(list1[i])
        f1.close()
    return list2

def final1(fname,list1,list2):  
    f1=open(fname, "r")
    list3=f1.readlines()
    len1=len(list1)
    len3=len(list3)
    for j in range(0,len1,1):
        year1=list1[j]
        f2=open(list2[j],"w")
        for i in range(0,len3,1):
            line1=list3[i]
            if year1 in line1:
                f2.write(line1)
        f2.close()
