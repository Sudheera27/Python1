f1=open("difficult.txt","w")
str1="Another day, and more cases reported from across the country. The number of COVID-19 cases tested positive in India is 156 and there are 139 active cases. According to WHO, as of March 17, there were 184,976 confirmed COVID-19 cases and 7,529 deaths in 159 countries.Chennai reported its second positive case today, West Bengal reported its first case yesterday, and the government of Goa made a *faux pas*.The State's health minister said a Norwegian national had tested positive but shortly afterwards retracted his remark."
list1=str1.split("*")
print(list1[1])
f1.write(list1[1])
f1.close()
