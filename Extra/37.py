f1=open("out1.txt","w")
upper=[]
lower=[]
for i in range(0,26,1):
    upper.append(chr(65+i))
    lower.append(chr(97+i))
upper1="\t".join(upper)
lower1=" ".join(lower)
print(upper1)
print(lower1)
f1.write(upper1)
f1.write("\n")
f1.write(lower1)
f1.close()
