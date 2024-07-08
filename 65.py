str1="Fun"
len1=len(str1)+1
spaces="-"
for i in range(0,3,1):
    print(spaces*(len1-i)+str1[0:i])+str1[i:leni-1]+spaces*(len1-i)

#print(spaces*1+"FUN"+"NUF"+spaces*1)
#print(spaces*2+"FU"+"UF"+spaces*2)
#print(spaces*3+"F"+"F"+spaces*3)
