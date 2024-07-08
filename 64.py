def diamond2(str2):
    len1=len(str2)
    for i in range(1,len1+1,1):
        spaces=" "*(len1-i)
        print(spaces,end="")
        print(str2[0:i])

    for i in range(1,len1,1):
        spaces=" "*i
        print(spaces,end="")
        print(str2[0:len1-i])
    print()
diamond2("Sudheera")
diamond2("Rahul")
diamond2("Rohit")




