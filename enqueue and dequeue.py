#enqueue = add a new item at the end (back of the line)
#dequeue = remove an item from the front (front of the line)
queue = []
queue.append('Bob')
queue.append('Alex')
queue.append('Quinn')
served = queue.pop(0)
print(queue)
print(served)

#check to prevent errors
if queue:
    served = queue.pop(0)


# enqueue one person
queue.append("Mia")

# dequeue twice
if queue:
    served1 = queue.pop(0)
    print('First served', served1)
else:
    print('Queue is empty')
if queue:
    served2 = queue.pop(0)
    print('Second served', served2)
else:
    print('Queue is empty')