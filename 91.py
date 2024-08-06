f1=open("olympics2.csv","r")
years1=[]
list1=f1.readlines()

for i in range(1,21000,1):
    list2=list1[i].split(",")
    year1=list2[0][0:4]
    years1.append(year1)
set1=set(years1)
years2=list(set1)
years2.sort()
print(years2)
