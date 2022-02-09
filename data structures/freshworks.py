Q. Given an array, find the maximum product sub array

[123] => 6

[013] => 3

[-1 2 3 -10 4]



[-2, 0, -2, 0]

max_in_array = 1
max_at_pos = 1
min_at_pos = 1

positive_flag = 0

for i in range(len(arr)):
    if arr[i] > 0:
        max_at_pos = max_at_pos * arr[i]
        min_at_pos = min(min_at_pos * arr[i], 1)
        positive_flag = 1
    else arr[i] == 0:
        max_at_pos = 1
        min_at_pos = 1
    else:
        a = max_at_pos
        max_at_pos = max(min_at_pos * arr[i], 1)
        min_at_pos = a * arr[i]

    if max_so_far < max_at_pos:
        max_so_far = max_at_pos

    if max_in_array == 1 and positive_flag == 0:
        return 0

    return max_so_far
