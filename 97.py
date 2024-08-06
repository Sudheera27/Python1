import mod_getyears as mg
infile1="olympics2.csv"
list1=mg.getyears(infile1)
list2=mg.createfiles(list1)
mg.final1(infile1,list1,list2)
