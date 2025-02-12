def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        print(f"Iteration {i + 1}:")
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        print(arr)
        if not swapped:
            break

data = [27, 15, 39, 21, 28, 70]
print("Initial data:", data)
bubble_sort(data)
print("Sorted data:", data)
