list1 = [10, 20, 30]


list2 = list1


list3 = list1.copy()

list1.append(40)

print("Original List:", list1)
print("Direct Assignment:", list2)
print("Using copy():", list3)
