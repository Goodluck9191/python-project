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

    # Delete first occurrence of value
    def delete_value(self, value):
        temp = self.head
        prev = None

        # If head node holds the value
        if temp is not None and temp.data == value:
            self.head = temp.next
            print(f"{value} deleted from the list.")
            return

        # Search for the value
        while temp is not None and temp.data != value:
            prev = temp
            temp = temp.next

        # If value not found
        if temp is None:
            print(f"{value} not found in the list.")
            return

        # Unlink the node
        prev.next = temp.next
        print(f"{value} deleted from the list.")

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

value = int(input("\nEnter value to delete: "))
ll.delete_value(value)

print("\nUpdated List:")
ll.display()