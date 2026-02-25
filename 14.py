class BankQueue:
    def __init__(self):
        self.queue = []

    # Enqueue customer
    def enqueue(self, customer_name):
        self.queue.append(customer_name)
        print(f"{customer_name} has joined the queue.")

    # Dequeue customer
    def dequeue(self):
        if len(self.queue) == 0:
            print("No customers in queue.")
        else:
            served = self.queue.pop(0)
            print(f"{served} has been served and left the bank.")

    # Display queue
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
        else:
            print("\nCurrent Queue Status:")
            for i, customer in enumerate(self.queue, start=1):
                print(f"{i}. {customer}")


# Main Program (User Interactive)
bank = BankQueue()

while True:
    print("\n--- BANK QUEUE MENU ---")
    print("1. Customer Arrives (Enqueue)")
    print("2. Serve Customer (Dequeue)")
    print("3. Display Queue")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter customer name: ")
        bank.enqueue(name)

    elif choice == 2:
        bank.dequeue()

    elif choice == 3:
        bank.display()

    elif choice == 4:
        print("Closing bank system.")
        break

    else:
        print("Invalid choice! Please try again.")