def rotateArray(arr: list, k: int) -> list:
    n = len(arr)
    k = k % n  # Normalize k
    return arr[k:] + arr[:k]  # Rotate by moving the first k elements to the end

arr = list(map(int, input().split()))
k = int(input())
print(rotateArray(arr, k))

