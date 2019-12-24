number = -32
soma = 0


if number < 0:
    number = number * (-1)

s = str(number)

for dig in s:
    soma += int(dig)

print(soma)