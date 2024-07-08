f1=open("Marks.txt","r")
names=[]
subjects=[]
sub1=[]
sub2=[]
topperSub1=[]
topperSub2=[]
for i in range(0,26,1):
    str1=f1.readline()
    list1=str1.split(",")
    names.append(list1[0])
    
    list2=list1[3].split(":")
    subjects.append(list2[0])
    sub1.append(int(list2[1]))

    list2=list1[4].split(":")
    subjects.append(list2[0])
    sub2.append(int(list2[1]))
maxSub1=max(sub1)
maxSub2=max(sub2)
for i in range(0,26,1):
    if sub1[i]==maxSub1:
        topperSub1.append(names[i])
    if sub2[i]==maxSub2:
        topperSub2.append(names[i])
print(topperSub1,"are the toppers in",subjects[0],"with",maxSub1,"marks")
print(topperSub2,"are the toppers in",subjects[1],"with",maxSub2,"marks")
print(sub1)
print(sub2)





