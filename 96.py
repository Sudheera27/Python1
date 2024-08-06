import mod_getyears as mg
list1=mg.getyears("olympics2.csv")
list2=mg.createfiles(list1)

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

final1("olympics2.csv",list1,list2)
