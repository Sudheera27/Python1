"""def check1(x):
    if x.endswith(".jpg"):
        return True
    return False"""
list1=["1.txt","2.txt","3.jpg"]
list2=list(filter(lambda x:True if x.endswith(".jpg") else False, list1))
print(list2)
