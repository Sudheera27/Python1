import os
dir1="C:/sample"
os.chdir(dir1)
list1=list(os.listdir())
list2=[]
list3=[]
for i in list1:
    if os.path.isdir(i):
        list2.append(i)
    else:
        list3.append(i)
print(list1)
print(list2)
print(list3)
