f1=open("convert.txt","r")
str1=f1.readline()
list1=str1.split(" ")
print(list1)

lhs_value=int(list1[0])
lhs_units=list1[1]
equals=list1[2]
rhs_value=int(list1[3])
rhs_units=list1[4]

line1="1 "+lhs_units+" "+equals+" "+str(rhs_value/lhs_value)+" "+rhs_units
line2="1 "+rhs_units+" "+equals+" "+str(lhs_value/rhs_value)+" "+lhs_units

print(line1)
print(line2)
