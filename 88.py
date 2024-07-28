list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list2=list(filter(lambda x: True if x%3 == 0 and x<10 else False,list1))
print(list2)

