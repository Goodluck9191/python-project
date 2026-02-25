class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []

    # Perform new action (Add text)
    def add_text(self, new_text):
        # Save current state before modifying
        self.undo_stack.append(self.text)
        self.text += new_text
        print("Text added successfully.")

    # Undo last action
    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo!")
        else:
            self.text = self.undo_stack.pop()
            print("Undo performed.")

    # Display current text
    def display(self):
        print("\nCurrent Text:")
        print(self.text if self.text else "[Empty Document]")


# Main Program (User Interactive)
editor = TextEditor()

while True:
    print("\n--- TEXT EDITOR MENU ---")
    print("1. Add Text")
    print("2. Undo")
    print("3. Display Text")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        new_text = input("Enter text to add: ")
        editor.add_text(new_text)

    elif choice == 2:
        editor.undo()

    elif choice == 3:
        editor.display()

    elif choice == 4:
        print("Closing editor.")
        break

    else:
        print("Invalid choice! Try again.")