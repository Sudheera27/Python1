str1="FunwithProgramming"
len1=len(str1)
for i in range(1,len1+1,1):
    spaces=" "*(len1-i)
    print(spaces,end="")
    print(str1[0:i])

for i in range(1,len1,1):
    spaces=" "*i
    print(spaces,end="")
    print(str1[0:len1-i])





