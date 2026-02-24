class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self,data):
        new_node = Node(data)
        if self.head is  None:
            self.head = new_node
        else:
            r = self.head
            while r.next is not None:
                r = r.next
            r.next = new_node
    
    def delete(self, value):
        if self.head.data == value:
            self.head = self.head.next
        
        r = self.head
        
        while r.next:
            if r.next.data == value:
                r.next = r.next.next
            r = r.next
    def display(self):
        r = self.head
        count = 0

        while r:
            print(r.data, end='->')
            
            r = r.next
            
        
        print('None')

li = LinkedList()
li.add(10)
li.add(20)
li.add(30)
li.display()
li.delete(20)
li.display()