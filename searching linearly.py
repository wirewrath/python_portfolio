# Searching Linearly [O(n)]
players = ["Priest", "Warrior", "Monk", "Paladin", "Mage", "Druid", "Hunter"]

steps = 0
for p in players:
    steps += 1
    if p == "Mage":
        print("Mage found!!")
        break
print("Steps used:", steps)

#enumerating items
items = ["sword", "bow", "shield", "potion"]

for index, item in enumerate(items):
    print(index, item)


def linear_search(items, target):
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1  # if we finish the loop without finding it. Sentinal value


items = ["sword", "bow", "shield", "potion"]
target = "potion"


def linear_search(items, target):
    for index, item in enumerate(items):
        if item == target:
            print(index, item)
            return index

    return -1


print(linear_search(items, target))
print(linear_search(items, "axe"))