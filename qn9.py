# Stack implementation using list

class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    # Push operation
    def push(self, value):
        if len(self.stack) >= self.size:
            print("Stack Overflow! Cannot push.")
        else:
            self.stack.append(value)
            print(f"{value} pushed into stack.")

    # Pop operation
    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow! Stack is empty.")
        else:
            removed = self.stack.pop()
            print(f"{removed} popped from stack.")

    # Display stack
    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty.")
        else:
            print("Stack elements (top to bottom):")
            for i in reversed(self.stack):
                print(i)


# Main Program (User Interactive)
size = int(input("Enter stack size: "))
s = Stack(size)

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to push: "))
        s.push(value)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.display()

    elif choice == 4:
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Please try again.")