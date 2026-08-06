stack = []
stack.append("sword")   # push
stack.append("shield")  # push
item = stack.pop()      # pop → "shield" (last in, first out)

queue = []
queue.append("Alice")   # join line
queue.append("Bob")
person = queue.pop(0)   # leave line → "Alice" (first in, first out)

from collections import deque

line = deque()

alice = {"name": "Alice", "pack": []}   # stack in pack
bob   = {"name": "Bob", "pack": []}

#line scenario

from collections import deque
line = deque()

alice = {"name": "Alice", "pack": ["map"]}
bob = {"name": "Bob", "pack": ["rope", "torch"]}

line.append(alice)
line.append(bob)

if line:
    front = line[0]
    if front["pack"]:
        used = front["pack"].pop()
        print(front["name"], "used", used)
    gone = line.popleft()
    print(gone["name"], "has left the line")

print("Current line", line)
print("Alice:", alice)
print("Bob", bob)

#adding a 3rd person with another checkpoint scenario
from collections import deque
line = deque()

alice = {"name": "Alice", "pack": ["map"]}
bob = {"name": "Bob", "pack": ["rope", "torch"]}
charlie = {"name": "Charlie", "pack": ["coin", "potion"]}

line.append(alice)
line.append(bob)
line.append(charlie)

if line:
    front = line[0]
    if front["pack"]:
        used = front["pack"].pop()
        print(front["name"], "used", used)
    gone = line.popleft()
    print(gone["name"], "has left the line")

if line:
    front = line[0]
    if front["pack"]:
        used = front["pack"].pop()
        print(front["name"], "used", used)
    gone = line.popleft()
    print(gone["name"], "has left the line")

print("Current line", line)
print("Alice:", alice)
print("Bob", bob)
print("Charlie", charlie)