def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr_input = input("Enter the numbers to sort (space-separated): ")
arr = list(map(int, arr_input.split()))

print("Original array:", arr)
insertion_sort(arr)
print("Sorted array:", arr)
