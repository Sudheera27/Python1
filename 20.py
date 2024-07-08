count=100
prison=["C"]*count
lucky=[]

for j in range(0,count,1):
    for i in range(j,count,j+1):
        if prison[i]=="C":
            prison[i]="O"
        else:
            prison[i]="C"
            
for i in range(0,count,1):
    if prison[i]=="O":
        lucky.append(i+1)
print(lucky,"are the lucky prisoners")
,,,
18
1,2,3,6,9,18 - 6 factors
25
1,5,25 - 3 factors
42
1,2,3,6,7,14,21,42 - 8 factors
48
1,2,3,4,6,8,12,16,24,48 - 10 factors
40
1,2,4,5,8,10,20,40 - 8 factors
8
1,2,4,8 - 4 factors
6
1,2,3,6 - 4 factors
2
1,2 - 2 factors
