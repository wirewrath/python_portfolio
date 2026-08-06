stack = []

if stack:                 # only True if stack is NOT empty
    item = stack.pop()
    print("Popped:", item)
else:
    print("Stack is empty, cannot pop!")

#empty stack
stack = []

#add to stack
stack.append("red")
stack.append("blue")
stack.append("green")
#safety check
if stack:
    last_color = stack.pop() #pop top item in stack
    print(last_color)
else:
    print("no stack")

print(stack)

#using undo
actions = []

actions.append("type 'Hello")
actions.append("type 'world")
actions.append("delet last word")
actions.append("type 'there'")
actions.pop()
actions.pop()
print(actions)
