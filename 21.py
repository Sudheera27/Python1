f1=open("Marks.txt","r")
names=[]
eng=[]
topperEng=[]
for i in range(0,26,1):
    str1=f1.readline()
    list1=str1.split(",")
    names.append(list1[0])
    list2=list1[3].split(":")
    eng.append(list2[1])
maxEng=max(eng)
for i in range(0,26,1):
    if eng[i]==maxEng:
        topperEng.append(names[i])
print(topperEng,"are the toppers in english with",maxEng,"marks")           
