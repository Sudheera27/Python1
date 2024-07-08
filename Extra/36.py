upper=[]
lower=[]
for i in range(0,26,1):
    upper.append(chr(65+i))
    lower.append(chr(97+i))
upper1="".join(upper)
lower1="".join(lower)
print(upper1)
print(lower1)
