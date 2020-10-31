
numList = []
numbers = [int(num) for num in input().split()]

sorted_num = sorted(numbers)
for num in sorted_num:
    if num >= 0:
        numList.append(num)
print(*numList, end=" ")