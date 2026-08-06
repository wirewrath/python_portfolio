# Using a list as a queue
line_list = []              # plain list
line_list.append("A")       # enqueue at the end
line_list.append("B")
first = line_list.pop(0)    # dequeue from the *front*
print("list queue:", line_list)

# Using deque as a queue
from collections import deque

line_deque = deque()        # deque object (queue-like)
line_deque.append("A")      # enqueue at the end
line_deque.append("B")
first2 = line_deque.popleft()  # dequeue from the *front*
print("deque queue:", line_deque)

#importing math
import math

number = 16
root = math.sqrt(number)

print("The square root of", number, "is", root)
#importing sqrt from math to use sqrt without math.sqrt
from math import sqrt

number = 16
root = sqrt(number)

print("The square root of", number, "is", root)
#append → adds to the back of the line
#popleft → serves/removes from the front of the line (FIFO ✅)
#pop would remove from the back, which is stack-like (LIFO), not what we want for a queue.
#appendleft adds to the front, which would break the normal queue behavior.

#building a list with the object deque and removing fifo
from collections import deque

names = deque()
names.append('Alice')
names.append('Bob')
names.append('Charlie')
print(names)

removed_names = names.popleft()

print(removed_names, "has been served")
print(names, "are still in line")
