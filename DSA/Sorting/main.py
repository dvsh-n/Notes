# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Time Complexity: O(n log n)
# Space Complexity: O(n)

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Time Complexity: O(n log n) on average, O(n^2) in the worst case
# Space Complexity: O(log n)

# Bucket Sort
def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    bucket_count = len(arr)
    max_value = max(arr)
    min_value = min(arr)

    # Create buckets
    buckets = [[] for _ in range(bucket_count)]

    # Distribute input array values into buckets
    for num in arr:
        index = int((num - min_value) / (max_value - min_value + 1) * bucket_count)
        buckets[index].append(num)

    # Sort individual buckets and concatenate
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))

    return sorted_array

# Time Complexity: O(n + k)
# Space Complexity: O(n + k)

# Example usage
if __name__ == "__main__":
    example_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", example_array)
    print("Bubble Sort:", bubble_sort(example_array.copy()))
    print("Selection Sort:", selection_sort(example_array.copy()))
    print("Insertion Sort:", insertion_sort(example_array.copy()))
    print("Merge Sort:", merge_sort(example_array.copy()))
    print("Quick Sort:", quick_sort(example_array.copy()))