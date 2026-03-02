
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None

    
    def create_list(self, n):
        for i in range(n):
            data = int(input(f"Enter data for node {i+1}: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new_node

   
    def insert_at_position(self, data, position):
        new_node = Node(data)

    
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for _ in range(position - 2):
            if temp is None:
                print("Position out of range!")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range!")
            return

        new_node.next = temp.next
        temp.next = new_node

    
    def display(self):
        temp = self.head
        if temp is None:
            print("List is empty.")
            return

        print("Linked List:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

ll = LinkedList()

n = int(input("Enter number of nodes: "))
ll.create_list(n)

print("\nOriginal List:")
ll.display()

data = int(input("\nEnter data to insert: "))
position = int(input("Enter position to insert at: "))

ll.insert_at_position(data, position)

print("\nUpdated List:")
ll.display()