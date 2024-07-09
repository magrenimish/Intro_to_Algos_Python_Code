def insertion_sort(arr):
    # Get the number of elements in the array
    n = len(arr)

    # Start from the second element as the first element is trivially sorted
    for i in range(1, n):
        # The current element to be inserted into the sorted portion of the array
        key = arr[i]
        # Start comparing with the element just before the current element
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        # of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key into its correct position in the sorted portion
        arr[j + 1] = key

# This code can be tested with:
# sample_array = [22, 27, 16, 9, 21]
# insertion_sort(sample_array)
# print("Sorted array is:", sample_array)
