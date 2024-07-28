list1=["1.txt","2.txt","3.jpg"]
#list2=list(filter(lambda x:True if x.endswith(".jpg") else False, list1))
#print(list2)
def check1(list1):
    list2=[]
    for i in range(0,3,1):
        if list1[i].endswith(".jpg"):
            list2.append(list1[i])
    return list2
print(check1(list1))

        
