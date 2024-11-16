def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    # Finding the middle point
    mid = len(arr) // 2
    
    # Dividing array into two halves
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursive calls to sort both halves
    merge_sort(left)
    merge_sort(right)
    
    # Merge the sorted halves
    merge(arr, left, right)
    
def merge(arr, left, right):
    i = j = k = 0
    
    # Compare and merge elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    # Handle remaining elements in left array
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    # Handle remaining elements in right array
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Example usage
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original array: {arr}")
    merge_sort(arr)
    print(f"Sorted array: {arr}")
