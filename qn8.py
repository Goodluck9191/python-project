
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

    
    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    
    def reverse(self):
        prev = None
        current = self.head
        next_node = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    
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


count = ll.count_nodes()
print("\nNumber of nodes:", count)


ll.reverse()
print("\nReversed List:")
ll.display()