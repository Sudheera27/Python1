f1=open("Marks.txt","r")
names=[]
subjects=[]
sub1=[]
topperSub1=[]
for i in range(0,26,1):
    str1=f1.readline()
    list1=str1.split(",")
    names.append(list1[0])
    list2=list1[3].split(":")
    subjects.append(list2[0])
    sub1.append(list2[1])
maxSub1=max(sub1)
for i in range(0,26,1):
    if sub1[i]==maxSub1:
        topperSub1.append(names[i])
print(topperSub1,"are the toppers in",subjects[0],"with",maxSub1,"marks")           
