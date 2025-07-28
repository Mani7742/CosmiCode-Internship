# Write a program that takes a list of numbers and finds the subarray with the maximum sum (Kadane's Algorithm).

def max_subarray_sum(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by space: ").split()))
    result = max_subarray_sum(arr)
    print(f"Maximum subarray sum is: {result}")




