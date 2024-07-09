def bubble_sort(arr):
    # Get the number of elements in the array
    n = len(arr)

    # Outer loop to traverse through all elements in the array
    for i in range(n - 1):
        # Inner loop to compare elements up to the point where the largest
        # elements have already bubbled to the end of the list
        for j in range(n - i - 1):
            # Compare adjacent elements and swap if they are in the wrong order
            if arr[j] > arr[j + 1]:
                # Swap elements using Python's tuple unpacking
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# This code can be tested with:
# sample_array = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(sample_array)
# print("Sorted array is:", sample_array)
