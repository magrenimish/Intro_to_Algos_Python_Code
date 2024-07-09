def selection_sort(arr):
    # Get the number of elements in the array
    n = len(arr)

    # Loop over the array to find the minimum element in each iteration
    for i in range(n - 1):
        # Assume the first element of the unsorted segment is the minimum
        min_idx = i
        
        # Compare the assumed minimum with the rest of the array
        for j in range(i + 1, n):
            # If a smaller element is found, update the index of the minimum element
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element of the unsorted segment
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# This code can be tested with:
# sample_array = [64, 25, 12, 22, 11]
# selection_sort(sample_array)
# print("Sorted array is:", sample_array)
