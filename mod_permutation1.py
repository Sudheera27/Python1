def perm3(s3):
    list3=[]
    c1=s3[0:1]
    c2=s3[1:2]
    c3=s3[2:3]
    list3.append(c1+c2+c3)
    list3.append(c1+c3+c2)
    list3.append(c2+c1+c3)
    list3.append(c2+c3+c1)
    list3.append(c3+c1+c2)
    list3.append(c3+c2+c1)
    return list3

def perm4(s4):
    list4=[]
    c1=s4[0:1]
    c2=s4[1:2]
    c3=s4[2:3]
    c4=s4[3:4]
    part1=c1
    part2=c2+c3+c4
    temp=perm3(part2)
    for i in range(0,6,1):
        list4.append(part1+temp[i])
    part1=c2
    part2=c1+c3+c4
    temp=perm3(part2)
    for i in range(0,6,1):
        list4.append(part1+temp[i])
    part1=c3
    part2=c1+c2+c4
    temp=perm3(part2)
    for i in range(0,6,1):
        list4.append(part1+temp[i])
    part1=c4
    part2=c1+c2+c3
    temp=perm3(part2)
    for i in range(0,6,1):
        list4.append(part1+temp[i])
    return list4

def perm5(s5):
    list5=[]
    c1=s5[0:1]
    c2=s5[1:2]
    c3=s5[2:3]
    c4=s5[3:4]
    c5=s5[4:5]
    part1=c1
    part2=c2+c3+c4+c5
    temp=perm4(part2)
    for i in range(0,24,1):
        list5.append(part1+temp[i])
    part1=c2
    part2=c1+c3+c4+c5
    temp=perm4(part2)
    for i in range(0,24,1):
        list5.append(part1+temp[i])
    part1=c3
    part2=c1+c2+c4+c5
    temp=perm4(part2)
    for i in range(0,24,1):
        list5.append(part1+temp[i])
    part1=c4
    part2=c1+c2+c3+c5
    temp=perm4(part2)
    for i in range(0,24,1):
        list5.append(part1+temp[i])
    part1=c5
    part2=c1+c2+c3+c4
    temp=perm4(part2)
    for i in range(0,24,1):
        list5.append(part1+temp[i])
    return list5















