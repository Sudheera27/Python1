def diamond1(str1):
    len1=len(str1)
    for i in range(1,len1+1,1):
        print(str1[0:i])
    for i in range(1,len1,1):
        print(str1[0:len1-i])
    print()

diamond1("Sudheera")
diamond1("Rohit")
diamond1("Rahul")

