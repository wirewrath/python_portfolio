players = [
    {"name": "Alice", "items": ["sword", "potion"]},
    {"name": "Bob", "items": ["shield"]},
]

quests = [
    {"name": "Goblin Hunt", "required_items": ["sword", "shield"]},
]

#long way of searching through everything
for quest in quests:
    for item in quest["required_items"]:
        for player in players:
            for p_item in player["items"]:
                if p_item == item:
                    print(player["name"], "has", item, "for", quest["name"])

players = ["Alice", "Bob", "Cara"]
banned_players = ["Bob", "Eve"]
#Another example of the long way
for player in players:
    for banned in banned_players:
        if player == banned:
            print(player, "is banned")
#short way by making a dictionary to track
banned_lookup = {}
for banned in banned_players:
    banned_lookup[banned] = True

for player in players:
    if player in banned_lookup:
        print(player, "is banned")

#using 2 loops with faster checking

players = ["Alice", "Bob", "Cara"]

bans = [
    {"name": "Bob", "reason": "cheating"},
    {"name": "Eve", "reason": "abuse"},
]

# 1. Build the ban_lookup dictionary
ban_lookup = {}
for ban in bans:
    ban_lookup[ban["name"]] = ban["reason"]

# 2. Loop over players and check the lookup dictionary
for player in players:
    if player in ban_lookup:
        # Retrieve the reason using the player's name as the key
        reason = ban_lookup[player]
        print(f"{player} is banned for {reason}")
#use nested loops for things like this
grid = [
    [1, 2, 3],
    [4, 5, 6],
]

for row in grid:
    for value in row:
        print(value)

players = ["Alice", "Bob", "Cara"]
scores = {"Alice": 10, "Bob": 15, "Cara": 7}

for player in players:
    for name in scores:
        if player == name:
            print(player, "has score", scores[name])
#cleaner version
for player in players:
    if player in scores:
        print(player, "has score", scores[player])
