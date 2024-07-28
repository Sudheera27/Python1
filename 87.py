list1=[1,2,3,4,5,6,7,8,9,10]
list2=list(filter(lambda x: True if x%3 == 0 else False,list1))
print(list2)

