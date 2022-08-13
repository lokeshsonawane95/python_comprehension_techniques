list1 = [1, 9, 5, 4, 7, 8, 3, 2, 0]
list1_copy = [x for x in list1]
print(list1_copy)

list2 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
list2_copy = [x for x in list2 if "o" in x]
print(list2_copy)

list2_copy2 = [x for x in list2 if x != "seven"]
print(list2_copy2)

list2_concatenate = [(x + x) for x in list2]
print(list2_concatenate)
