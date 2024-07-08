f1=open("passage.txt","r")
str1=f1.readline().replace("\n","").lower()
list1=str1.split(" ")
set1=set(list1)
list2=list(set1)
list2.sort()
print(list2)

