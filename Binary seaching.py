def binary_search(numbers, target):
    low = 0
    high = len(numbers) -1

    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] > target:
            high = mid -1
        else:
            low = mid + 1
    return -1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
target = 11

print(binary_search(numbers, target))

unsorted_numbers = [14, 7, 8, 10, 9, 1, 2, 6, 5, 3, 4, 12, 11, 13]

"""unsorted_numbers.sort() 
numbers = unsorted_numbers""" #This is one way to sort a list of unsorted numbers.
target = 11
#another way to sort
numbers = sorted(unsorted_numbers)

print(binary_search(numbers, target))
