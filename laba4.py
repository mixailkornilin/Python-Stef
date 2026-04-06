def R_S(arr, ind, acc):
    if ind == len(arr):
        return acc
    return R_S(arr, ind +1, acc + arr[ind])

def max_val(arr, ind, cur_max):
    if ind == len(arr):
        return cur_max
    if arr[ind] > cur_max:
        cur_max = arr[ind]
    return max_val(arr, ind + 1, cur_max)

def min_val(arr, ind, cur_min):
    if ind == len(arr):
        return cur_min
    if arr[ind] < cur_min:
        cur_min = arr[ind]
    return min_val(arr, ind + 1, cur_min)

arr1 = [1,4,2,3,56]
mins = min_val(arr1, 0, arr1[0])
maxs = max_val(arr1, 0, arr1[0])
result = R_S(arr1, 0, 0)

print('sum:', result, 'min:', mins, 'max:', maxs)

for n in range(100):
    for m in range(100):
        if n**2 + m == 99: #n^2 + m = 99
            print(n, m)
