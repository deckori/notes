c0 = int(input("Input a natural number: "))

steps = 1

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2

        if c0 == 1:
            print(c0)
            break
        print(c0, end=",")

        steps += 1
        continue
    else:
        c0 = (c0 * 3) + 1

        if c0 == 1:
            print(c0)
            break
        print(c0, end=",")

        steps += 1
        continue
print("steps = ", steps)
