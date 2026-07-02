input_list = []

while len(input_list) < 3:
    num = int(input("Enter a number: "))
    input_list.append(num)


def tri_exponent(some_list):
    global sum
    sum = 2 ** some_list[0] + 2 ** some_list[1] + 2 ** some_list[2]
    return sum


tri_exponent(input_list)

print(sum)
