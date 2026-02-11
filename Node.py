class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#Linked List class

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

li = LinkedList()
li.insert_begin(10)
li.insert_begin(20)
li.insert_begin(30)
li.insert_begin(40)
li.display()
        