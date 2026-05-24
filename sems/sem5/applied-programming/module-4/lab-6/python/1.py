var = int(input("Enter a number: "))
result_mul = var << 2
result_div = var >> 1
result_mod = var & 1

print(var, "*4 = ", result_mul, ", ", var, " // 2 = ", result_div, ", ", var, " % 2 = ", result_mod, sep="")
