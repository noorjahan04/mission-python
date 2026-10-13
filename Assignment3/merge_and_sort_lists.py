# list1=[1,4,7]
# list2=[2,5,6]
# result=list1+list2
# result.sort()
# print(result)


list1 = input("Enter first list numbers: ").split()
list2 = input("Enter second list numbers: ").split()

result = list1 + list2
result = [int(num) for num in result]

result.sort()

print("Sorted list:", result)
