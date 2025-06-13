def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr_input = input("Provide the number list (space-separated): ")
arr = list(map(int, arr_input.split()))

target = int(input("Enter the number to be searched: "))

result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
