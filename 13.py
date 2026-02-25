class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    # Enqueue operation
    def enqueue(self, value):
        if self.rear == self.size - 1:
            print("Queue Overflow! Cannot insert element.")
            return

        if self.front == -1:  # First element insertion
            self.front = 0

        self.rear += 1
        self.queue[self.rear] = value
        print(f"{value} inserted into queue.")

    # Dequeue operation
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow! Queue is empty.")
            return

        removed = self.queue[self.front]
        self.front += 1
        print(f"{removed} removed from queue.")

    # Display queue
    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty.")
            return

        print("Queue elements:")
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")
        print()


# Main Program (User Interactive)
size = int(input("Enter queue size: "))
q = Queue(size)

while True:
    print("\n--- QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to enqueue: "))
        q.enqueue(value)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.display()

    elif choice == 4:
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Try again.")