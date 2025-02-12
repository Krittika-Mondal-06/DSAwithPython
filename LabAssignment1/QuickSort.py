def quick_sort(arr, low, high, depth=1):
    if low < high:
        pivot_index = partition(arr, low, high)
        print(f"Iteration {depth}: {arr}")
        quick_sort(arr, low, pivot_index - 1, depth + 1)
        quick_sort(arr, pivot_index + 1, high, depth + 1)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:  # Changed < to <= to handle duplicate values better
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

data = [27, 15, 39, 21, 28, 70]
quick_sort(data, 0, len(data) - 1)
print("Sorted array:", data)