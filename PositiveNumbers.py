# First input list
list1 = [12, -7, 5, 64, -14]
print("Input: list1 =", list1)
print("Output:", end=" ")
for num in list1:
    if num > 0:
        print(num, end=", ")
print("\n")

# Second input list
list2 = [12, 14, -95, 3]
print("Input: list2 =", list2)
positive_nums = [num for num in list2 if num > 0]
print("Output:", positive_nums)
