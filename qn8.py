# Define Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Define Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Create linked list
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

    # Count nodes
    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    # Reverse linked list
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

    # Display linked list
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


# Main Program (User Interactive)
ll = LinkedList()

n = int(input("Enter number of nodes: "))
ll.create_list(n)

print("\nOriginal List:")
ll.display()

# Count nodes
count = ll.count_nodes()
print("\nNumber of nodes:", count)

# Reverse list
ll.reverse()
print("\nReversed List:")
ll.display()