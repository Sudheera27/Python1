f1=open("out1.txt","w")
upper=[]
lower=[]
num_upper=[]
num_lower=[]
for i in range(0,26,1):
    upper.append(chr(65+i))
    lower.append(chr(97+i))
for i in range(0,26,1):
    num_upper.append(ord(upper[i]))
    num_lower.append(ord(lower[i]))
upper1=" ".join(upper)
lower1=" ".join(lower)
print(upper)
print(lower)
print(num_upper)
print(num_lower)
f1.write(upper1)
f1.write("\n")
f1.write(lower1)
f1.write("\n")
f1.close()
