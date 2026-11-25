list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

common = []

for i in list1:
    if i in list2 and i not in common:
        common.append(i)

print("Common Elements:", common)
