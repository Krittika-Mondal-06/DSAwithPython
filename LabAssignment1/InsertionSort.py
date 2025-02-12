def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Iteration {i}: {arr}")

data = [27, 15, 39, 21, 28, 70]
print("Initial array:", data)
insertion_sort(data)
print("Sorted array:", data)
