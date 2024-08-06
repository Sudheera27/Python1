import mod_getyears as mg
list1=mg.getyears("olympics2.csv")
len1=len(list1)
fname1="olympics2_"
fname3=".csv"
for i in range (0,len1,1):
    fname=fname1+list1[i]+fname3
    f1=open(fname,"w")
    f1.write(list1[i])
    f1.close()
