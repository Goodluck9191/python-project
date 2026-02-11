class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.next = third

r = head
print('Linked list')

while r is not None:
    print(r.data, end="->")
    r = r.next

print('None')




        