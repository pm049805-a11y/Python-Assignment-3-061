numbers = [10, 15, 20, 25, 30, 35]

even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers =", even)
print("Odd numbers =", odd)
