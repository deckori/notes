names = []
for i in range(4):
    name = input("Enter a name: ")
    names.append(name)

print("List:", names)
names.sort()
print("Sorted:", names)
names.reverse()
print("Reversed:", names)
print("Length:", len(names))
