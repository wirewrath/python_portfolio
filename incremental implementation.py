def get_even_numbers(numbers):
    # 1. Create an empty list to store the even numbers
    even_list = []

    # 2. Loop through each number in the list
    for num in numbers:
        # 3. Check if the number is even (divisible by 2)
        if num % 2 == 0:
            even_list.append(num)

    # 4. Return the finished list
    return even_list


# Quick test check
test_numbers = [1, 2, 3, 4, 5, 6]
print(get_even_numbers(test_numbers))

# 1. Define the new function
def average_even_numbers(numbers):
    # 2. Use your existing function to get only the evens
    evens = get_even_numbers(numbers)

    # 3. Handle the edge case: if the list is empty, return None
    if len(evens) == 0:
        return None

    # 4. Calculate and return the average
    total = sum(evens)
    average = total / len(evens)
    return average


# 5. Manual test checks
print(average_even_numbers([1, 2, 3, 4]))  # Expected output: 3.0
print(average_even_numbers([1, 3, 5]))  # Expected output: None