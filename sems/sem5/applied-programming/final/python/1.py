input_list = []

while True:
    user_input = input(
        "Type an integer number or type any letter to finish inputting values to the list: "
    )

    try:
        number = int(user_input)
        input_list.append(number)
    except ValueError:
        print("The new list is", input_list)
        break

undup_list = []
dup_only_list = []

for i in input_list:
    if i not in undup_list:
        undup_list.append(i)
    elif i not in dup_only_list and i in undup_list:
        dup_only_list.append(i)

print(dup_only_list)
