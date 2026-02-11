class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            r = self.head

            while r.next is not None:
                r = r.next
            r.next = new_node


    def delete_value(self, value):
        if self.head.data == value:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next:
            if temp.next.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next


    

    def display(self):
        r = self.head
        while r:
            print(r.data, end="->")
            r = r.next
        print("NOne")
    

li = Linkedlist()
li.add(10)
li.add(20)
li.add(30)
li.display()
li.delete_value(10)
li.display()