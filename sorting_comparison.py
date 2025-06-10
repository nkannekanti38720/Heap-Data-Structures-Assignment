import random
import time
from heapsort import heapsort  # Import the heapsort function

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def measure_time(func, arr):
    start = time.time()
    func(arr)
    end = time.time()
    return end - start

# Testing comparison
arr = [random.randint(1, 1000) for _ in range(1000)]

print("Heapsort Time:", measure_time(heapsort, arr.copy()))
print("Quicksort Time:", measure_time(quicksort, arr.copy()))
print("Mergesort Time:", measure_time(mergesort, arr.copy()))
