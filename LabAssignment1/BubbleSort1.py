import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:  # Changed < to <= for better handling of duplicates
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

data_size = 1000
data1 = [random.randint(1, 10000) for _ in range(data_size)]
data2 = data1.copy()  # Create a *separate* copy for quick sort

start_time = time.time()
bubble_sort(data1)
bubble_time = time.time() - start_time

start_time = time.time()
quick_sort(data2, 0, len(data2) - 1)
quick_time = time.time() - start_time

print(f"Bubble Sort Time: {bubble_time:.6f} seconds")
print(f"Quick Sort Time: {quick_time:.6f} seconds")

if quick_time < bubble_time:  # More robust comparison
    print("Quick Sort is generally faster than Bubble Sort for large datasets!")
elif quick_time > bubble_time:
    print("Bubble Sort was faster in this specific run (rare, but possible).")
else:
    print("The sorting times were approximately equal.")