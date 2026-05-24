List1 = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print(List1)

List2 = []

for item in List1:
    if item not in List2:
        List2.append(item)

print(List2)
