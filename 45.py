f1=open("passage.txt","r")
f2=open("sorted_passage.txt","w")
str1=f1.readline().replace("\n","").lower()
list1=str1.split(" ")

set1=set(list1)
list2=list(set1)
list2.sort()
for i in range(0,len(list2),1):
    f2.write(list2[i])
    f2.write("\n")
f2.close()
print(list2)

