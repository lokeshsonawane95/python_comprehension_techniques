dictionary1 = {x: x ** 2 for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]}
print(dictionary1)

dictionary2 = {x: x ** 3 for x in range(10)}
print(dictionary2)

dictionary3 = {x: x.upper() for x in "upper"}
print(dictionary3)

dictionary4 = {x: x ** 2 for x in range(10) if x ** 2 % 2 != 0}
print(dictionary4)

dictionary5 = {x: x ** 3 for x in range(10) if x ** 3 % 3 == 0}
print(dictionary5)
