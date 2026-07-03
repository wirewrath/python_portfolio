drops = ["coin", "gem", "coin", "potion", "coin"]
counts = {}

for drop in drops:
    if drop in counts:
        counts[drop] += 1
    else:
        counts[drop] = 1

print(counts)

for drop in drops:
    counts[drop] = counts.get(drop, 0) + 1
print(counts)
#alternate short method

rounds = [
    ("arya", 10),
    ("ben", 5),
    ("arya", 7),
    ("ben", 3),
]
scores = {}

for player, points in rounds:
    scores[player] = scores.get(player, 0) + points
print(scores)
# adding player scores

finds = [
    ("forest", "mushroom"),
    ("cave", "bat"),
    ("forest", "wolf"),
    ("cave", "gem"),
    ("river", "fish")
]

groups = {}

for place, item in finds:
    if place not in groups:
        groups[place] = []
    groups[place].append(item)

print(groups)
#grouping

pets = ["cat", "dog", "cat", "bird", "dog", "cat"]
pet_counts = {}

for pet in pets:
    pet_counts[pet] = pet_counts.get(pet, 0) + 1

print(pet_counts)

players = [
    ("Alice", "hall"),
    ("Bob", "kitchen"),
    ("Cara", "hall"),
]

rooms = {}
for name, room in players:
    rooms[room] = rooms.get(room, []) + [name]

print(rooms)