c0 = int(input("Type in any number: "))

steps=1

while c0 > 0:

    if c0 % 2 == 0:
        c0 = int(c0/2)

        if c0 == 1:
            print(c0)
            break

        print(c0, end=",")

        steps+=1
        continue

    elif c0 % 2 != 0:
        c0 = int(3 * c0 + 1)

        if c0 == 1:
            print(c0)
            break

        print(c0, end=",")

        steps+=1
        continue

print("steps =", steps)
