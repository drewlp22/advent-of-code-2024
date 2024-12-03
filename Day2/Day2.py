def checksafe(arr):
    # check one direction
    try:
        n = len(arr)
    except TypeError:
        return True
    is_increasing = True
    is_decreasing = True

    for i in range(1, n):
        if arr[i - 1] < arr[i] and is_decreasing:
            is_decreasing = False
        if arr[i - 1] > arr[i] and is_increasing:
            is_increasing = False
        if abs(arr[i - 1] - arr[i]) > 3:
            return False
        elif abs(arr[i - 1] - arr[i]) == 0:
            return False

    if not (is_decreasing or is_increasing):
        return False

    return True

input = [
[7, 6, 4, 2, 1],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[1, 3, 2, 4, 5],
[8, 6, 4, 4, 1],
[1, 3, 6, 7, 9],
[0, 5]
]

count = 0

file = open("Day2.txt", 'r')

for line in file:
    str_nums = line.split()
    nums = [int(num) for num in str_nums]
    if checksafe(nums):
        count += 1
        continue
        
    n = len(nums)
    for i in range(0, n):
        new_nums = nums.copy()
        new_nums.pop(i)
        if checksafe(new_nums):
            count += 1
            break

# for line in file:
#     str_nums = line.split()
#     nums = [int(num) for num in str_nums]
#     if checksafe(nums):
#         count += 1

print(count)

