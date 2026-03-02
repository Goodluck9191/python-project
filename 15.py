class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    
    def enqueue(self, value):
        
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow! No space available.")
            return

        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = value
        print(f"{value} added to the queue.")

    
    def dequeue(self):
        
        if self.front == -1:
            print("Queue Underflow! Queue is empty.")
            return

        removed = self.queue[self.front]
        self.queue[self.front] = None

        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(f"{removed} removed from the queue.")

    
    def display(self):
        if self.front == -1:
            print("Queue is empty.")
            return

        print("Queue elements:")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()



size = int(input("Enter size of circular queue: "))
cq = CircularQueue(size)

while True:
    print("\n--- CIRCULAR QUEUE MENU ---")
    print("1. Enqueue (Add Resource)")
    print("2. Dequeue (Release Resource)")
    print("3. Display Queue")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = input("Enter resource name: ")
        cq.enqueue(value)

    elif choice == 2:
        cq.dequeue()

    elif choice == 3:
        cq.display()

    elif choice == 4:
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Try again.")