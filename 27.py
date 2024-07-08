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
    print(topperSub1,"are the toppers in",subjects[0],"with",maxSub1,"marks")
    print(topperSub2,"are the toppers in",subjects[1],"with",maxSub2,"marks")
    print(topperSub3,"are the toppers in",subjects[2],"with",maxSub3,"marks")
    print(topperSub4,"are the toppers in",subjects[3],"with",maxSub4,"marks")
    print(topperSub5,"are the toppers in",subjects[4],"with",maxSub5,"marks")
    print(goldMedalist,"are the gold medalists with",maxTotal,"marks")
    print()
goldMedal1("Marks.txt")
goldMedal1("Marks2.txt")



