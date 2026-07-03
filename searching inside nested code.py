players = [
    {"name": "Ayla", "level": 5, "class": "Mage"},
    {"name": "Borin", "level": 12, "class": "Warrior"},
    {"name": "Cira", "level": 18, "class": "Rogue"},
    {"name": "Dane", "level": 3, "class": "Mage"},
]
high_level_players = []          # 1) start an empty results list

for player in players:           # 2) scan each player
    if player["level"] >= 10:    # 3) test the rule
        high_level_players.append(player)  # 4) collect matches
mages = []
for player in players:
    if player["class"] == "Mage":
        mages.append(player)
print(mages)
# easier way to read the code
def is_mage(player):
    return player["class"] == "Mage"

mages = []

for player in players:
    if is_mage(player):      # just reads like English now
        mages.append(player)

high_level_warriors = []

def is_high_level_warrior(player):
    return player["class"] == "Warrior" and player["level"] >= 10

for player in players:
    if is_high_level_warrior(player):
        high_level_warriors.append(player)
print(high_level_warriors)

#using if else instead
def is_high_level_warrior(player):
    if player["class"] == "Warrior" and player["level"] >= 10:
        return True
    else:
        return False