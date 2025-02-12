import time
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid].copy()  # Create copies of subarrays
        right_half = arr[mid:].copy() # Create copies of subarrays

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]: # Changed < to <=
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:  # Changed < to <= for better duplicate handling
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

data_size = 1000
data1 = [random.randint(1, 10000) for _ in range(data_size)]
data2 = data1.copy()

start_time = time.time()
merge_sort(data1)
merge_time = time.time() - start_time

start_time = time.time()
quick_sort(data2, 0, len(data2) - 1)
quick_time = time.time() - start_time

print(f"Merge Sort Time: {merge_time:.6f} seconds")
print(f"Quick Sort Time: {quick_time:.6f} seconds")

if merge_time < quick_time: # Corrected the comparison logic
    print("Merge Sort is generally more effective than Quick Sort for stable sorting and larger datasets!")
elif merge_time > quick_time:
    print("Quick Sort was faster in this specific run.")
else:
    print("The sorting times were approximately equal.")