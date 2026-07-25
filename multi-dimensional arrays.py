grid = [
    [".", ".", "#"],
    [".", "P", "."],
    ["#", ".", "."]
]
#updating the grid
grid[1][1] = "."   # clear old player spot
grid[1][2] = "P"   # new player spot

#creating a grid and updating
grid = [
    [".", ".", "."],
    [".", "P", "."],
    [".", ".", "."]
]
grid[0][0] = "#"
print(grid)
#using a nested loop to search the grid and update
grid2 = [
    ['.', '.', '.'],
    [',', 'P', '.'],
    ['.', '.', '.']
]

for r in range(len(grid2)):
    for c in range(len(grid2[r])):
        if grid2[r][c] == '.':
            grid2[r][c] = '@'
print(grid2)

#updating the position of 'P'
grid = [
    [".", ".", "#"],
    [".", "P", "."],
    ["#", ".", "."]
]
#clear the old spot
grid[1][1] = "."

#set the new player spot
grid[2][1] = "P"

print(grid)

#protection against index error
r = 2
c = 1

if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
    grid[r][c] = "X"

# Create a sample list to test with
items = ["apple", "banana", "cherry"]

# 1. Safely print the first element (index 0)
if len(items) >= 1:
    print("First element:", items[0])

# 2. Safely print the third element (index 2)
if len(items) >= 3:
    print("Third element:", items[2])

# Create a sample list of scores to test with
scores = [1200, 950, 800]

# Check if there are at least 3 scores
if len(scores) >= 3:
    print("Top 1:", scores[0])
    print("Top 2:", scores[1])
    print("Top 3:", scores[2])
else:
    print("Not enough scores yet!")

scores = [1200, 950, 800]

# Loop up to 3 times, or up to len(scores) if there are fewer than 3
for i in range(min(3, len(scores))):
    print(f"Top {i + 1}: {scores[i]}")