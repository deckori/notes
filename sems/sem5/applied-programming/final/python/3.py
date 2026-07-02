numbers = []

while len(numbers) < 3:
    number = int(input("Enter your number: "))

    numbers.append(number)


def tri_square_sum(some_list):
    global sum
    sum = some_list[0] ** 2 + some_list[1] ** 2 + some_list[2] ** 2
    return sum


tri_square_sum(numbers)
print(sum)
