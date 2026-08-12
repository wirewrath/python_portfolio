names = ["Alice", "Bob", "Charlie", "Thomas", "Zoe"]
target = "Thomas"
steps = 0

for name in names:
    steps = steps + 1 #counting the amount of steps the code makes in total
    if name == target:
        print("Found!")
        break #stop the loop once the target is found

print(steps)

#complex algorithm

numbers = list(range(1, 100001))  # numbers 1 to 100000
target = 100000

def search_by_hand(numbers, target):
    checks = 0
    for num in numbers:
        checks += 1
        if num == target:
            return True, checks
    return False, checks

def search_with_set(numbers, target):
    checks = 0
    numbers_set = set(numbers)
    checks += 1
    found = target in numbers_set

    return found, checks

found_hand, checks_hand = search_by_hand(numbers, target)
print(f"Hand search -> Found: {found_hand}, Checks made: {checks_hand}")

found_set, checks_set = search_with_set(numbers, target)
print(f"Set search -> Found: {found_set}, Checks made: {checks_set}")