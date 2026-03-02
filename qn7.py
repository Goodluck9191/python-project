
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

    
    def delete_value(self, value):
        temp = self.head
        prev = None

        
        if temp is not None and temp.data == value:
            self.head = temp.next
            print(f"{value} deleted from the list.")
            return

        
        while temp is not None and temp.data != value:
            prev = temp
            temp = temp.next

        
        if temp is None:
            print(f"{value} not found in the list.")
            return

        
        prev.next = temp.next
        print(f"{value} deleted from the list.")

    
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

value = int(input("\nEnter value to delete: "))
ll.delete_value(value)

print("\nUpdated List:")
ll.display()