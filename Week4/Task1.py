# Implement a binary search algorithm to find the position of a target value within a sorted list.
def binary_search(arr, target):
    """
    Perform binary search on a sorted list to find the index of the target value.
    Returns the index if found, else returns -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage:
if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11, 13]
    target = 7
    result = binary_search(sorted_list, target)
    print(f"Index of {target}: {result}")