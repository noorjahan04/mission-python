
list1 = [1, 2, 3, 2, 4, 3, 5, 1]

seen = set()
duplicates = set()

for num in list1:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicate elements:", duplicates)
