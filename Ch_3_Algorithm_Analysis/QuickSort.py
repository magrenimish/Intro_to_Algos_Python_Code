def quick_sort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

def partition(arr, low, high):
    # This is the pivot element
    pivot = arr[high]
    i = (low-1)  # index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

# Example:
# arr = [10, 80, 30, 90, 40, 50, 70]
# quick_sort(arr, 0, len(arr)-1)
# print("Sorted array is:", arr)
