list1=[1,2,3,4]
list2=[5,6,7,8]
if set(list1).isdisjoint(set(list2)):
    print("The list shares no common elements")
else:
    print("The list shares common elements")