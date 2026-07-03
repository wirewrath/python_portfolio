scores = {
    "shadow": 175,
    "nova": 220,
    "pixel": 140
}
print(scores['nova'])

inventory = {
    'potion': 3,
    'sword': 1,
    'torch': 5
}
inventory["potion"] = 4      # update existing key
inventory["shield"] = 1      # add new key

print(inventory)
print(inventory['potion'])
print(inventory['torch'])
print(inventory.get("sword"))

if "shield" in inventory:
    print(inventory["shield"])
else:
    print("No shield found")

player = {}
player['name'] = 'Wirewrath'
player['level'] = 50
player['coins'] = 12
print(player.get('level'))
if 'level' in player:
    print(player['level'])
else:
    print('Level missing')

inventory = {"potion": 3, "torch": 5, "rope": 1}

for item, quantity in inventory.items():
    print(item, quantity)
#a printing loop that runs through the whole dictionary.

total = 0

for quantity in inventory.values():
    total = total + quantity

print(total)
#adds up total quantity in dictionary

scores = {"arya": 10, "blake": 7, "cora": 13}

total = 0

for quantity in scores.values():
    total = total + quantity

print(total)
#adds up total quantity in dictionary
for player in scores.keys():
    print(player)
    #for loop printing the player names

for player, score in scores.items():
    print(player, "scored", score)
    #prints both keys and values by using .items()

inventory = {"potion": 3, "torch": 5, "rope": 1}

for item, quantity in inventory.items():
    print(item,':',quantity)

total = 0
for quantity in inventory.values():
    total = total + quantity
print("Total:" ,total)
#.keys() when you need names/labels
#.values() when you need the stored data
#.items() when you need both together

players = [
    {"name": "wirewrath", "score": 12000, "level": 59},
    {"name": "shadow", "score": 900, "level": 19},
    {"name": "vixo", "score": 120, "level": 6}
]
print(players)
#when you need multiple dictionaries in a list.
