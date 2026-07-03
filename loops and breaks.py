numbers = [3, 7, -2, 10]
found_negative = False

for n in numbers:
    if n < 0:
        found_negative = True
        break  # stop the loop right now

print(found_negative)

scores = [5, 8, 12, 20, 4, 7]

total = 0

for score in scores:
    total += score
    if total >= 20:
        break

print(total)

scores = [5, 8, 12, 20, 4, 7]

total = 0
reached_limit = False

for score in scores:
    total += score
    if total >= 20:
        reached_limit = True
        break

print(total)
print(reached_limit)

numbers = [1, 2, 3, 4, 5]

found_even = False
total = 0

for n in numbers:
    total += n      # add current number
    if n % 2 == 0:  # is it even?
        found_even = True
        break
numbers = [1, 2, 3, 4, 5]

found_even = False

total = 0

for n in numbers:
    total += n
    if n % 2 == 0:
        found_even = True
        break

print(total)
print(found_even)

raw_users = ["  alice  ", "BOB", "  ChArLiE"]

# 1. Define the helper function
def clean_username(name):
    # .strip() removes whitespace, .lower() makes it lowercase
    return name.strip().lower()

# Create an empty list to collect the cleaned names
cleaned_users = []

# 2. Write the for loop over raw_users
for s in raw_users:
    cleaned_name = clean_username(s)   # call helper for this one score
    cleaned_users.append(cleaned_name)  # add it to our new list

# Print the final result after the loop completes
print(cleaned_users)