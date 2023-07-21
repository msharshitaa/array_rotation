def array_rotation(arr, k):
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]

arr = list(map(int, input().split()))
k = int(input())

rotated_arr = array_rotation(arr, k)
print(rotated_arr)
