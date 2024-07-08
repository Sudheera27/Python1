def goldMedal1(fname):
    f1=open(fname,"r")
    names=[]
    subjects=[]
    sub1=[]
    sub2=[]
    sub3=[]
    sub4=[]
    sub5=[]
    total=[]
    topperSub1=[]
    topperSub2=[]
    topperSub3=[]
    topperSub4=[]
    topperSub5=[]
    goldMedalist=[]
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
        list2=list1[5].split(":")
        subjects.append(list2[0])
        sub3.append(int(list2[1]))
        list2=list1[6].split(":")
        subjects.append(list2[0])
        sub4.append(int(list2[1]))
        list2=list1[7].split(":")
        subjects.append(list2[0])
        sub5.append(int(list2[1]))
        total.append(sub1[i]+sub2[i]+sub3[i]+sub4[i]+sub5[i])
    maxSub1=max(sub1)
    maxSub2=max(sub2)
    maxSub3=max(sub3)
    maxSub4=max(sub4)
    maxSub5=max(sub5)
    maxTotal=max(total)
    for i in range(0,26,1):
        if sub1[i]==maxSub1:
            topperSub1.append(names[i])
        if sub2[i]==maxSub2:
            topperSub2.append(names[i])
        if sub3[i]==maxSub3:
            topperSub3.append(names[i])
        if sub4[i]==maxSub4:
            topperSub4.append(names[i])
        if sub5[i]==maxSub5:
            topperSub5.append(names[i])
        if total[i]==maxTotal:
            goldMedalist.append(names[i])
    return(topperSub1,topperSub2,topperSub3,topperSub4,topperSub5,maxSub1,maxSub2,maxSub3,maxSub4,maxSub5)
result=goldMedal1("Marks.txt")
    
print(result[0],result[5])
print(result[1],result[6])
print(result[2],result[7])
print(result[3],result[8])
print(result[4],result[9])


