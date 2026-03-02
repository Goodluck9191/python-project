

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.next = third


current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")