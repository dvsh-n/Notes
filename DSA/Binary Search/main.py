# This module implements iterative and recursive binary search algorithms.
#
# Functions:
#     binary_search_iterative(arr, target):
#         Performs binary search on a sorted array iteratively.
#         Parameters:
#             arr (list): A sorted list of elements to search.
#             target (int/float): The element to search for in the array.
#         Returns:
#             int: The index of the target element if found, otherwise -1.
#         Time Complexity: O(log n), where n is the number of elements in the array.
#         Space Complexity: O(1), as it uses a constant amount of space.

#     binary_search_recursive(arr, target, left, right):
#         Performs binary search on a sorted array recursively.
#         Parameters:
#             arr (list): A sorted list of elements to search.
#             target (int/float): The element to search for in the array.
#             left (int): The starting index of the subarray to search.
#             right (int): The ending index of the subarray to search.
#         Returns:
#             int: The index of the target element if found, otherwise -1.
#         Time Complexity: O(log n), where n is the number of elements in the array.
#         Space Complexity: O(log n), due to the recursive call stack.


# Iterative Binary Search
def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Recursive Binary Search
def binary_search_recursive(arr, target, left, right):
    if left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, right)
        else:
            return binary_search_recursive(arr, target, left, mid - 1)
    return -1

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 10

    # Iterative search
    result_iterative = binary_search_iterative(arr, target)
    print(f"Iterative: Element {target} is at index {result_iterative}")

    # Recursive search
    result_recursive = binary_search_recursive(arr, target, 0, len(arr) - 1)
    print(f"Recursive: Element {target} is at index {result_recursive}")