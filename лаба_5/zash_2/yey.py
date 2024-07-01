arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_arr = []

cur_ind = 0
is_end = False
while not is_end:
    if cur_ind < len(arr):
        while cur_ind < len(arr) and arr[cur_ind] is None:
            cur_ind += 1

        if cur_ind == len(arr) and arr[cur_ind - 1] is None:
            is_end = True
        if not is_end:
            new_arr.append(arr[cur_ind])
            arr[cur_ind] = None
            cur_ind += 4
    else:
        cur_ind = 0

new_arr.append(new_arr[0])
print(new_arr)