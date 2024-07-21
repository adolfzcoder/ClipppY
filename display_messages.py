import tkinter as tk
from tkinter import scrolledtext

def display_clipboard():

    def extract_messages(filename):
        messages = []  # List to store all extracted messages
        current_message = []  # Store current messages

        with open(filename, "r") as file:
            inside_message = False

            for line in file:
                line = line.strip()  # Remove leading/trailing whitespace

                if line == "Start":
                    inside_message = True
                    current_message = []  # Reset current message

                elif line == "UniqueEndMsgLOL":
                    inside_message = False
                    # Join lines and append to messages
                    messages.append("".join(current_message))
                    current_message = []  # Reset current message

                elif inside_message:
                    current_message.append(line)

        return messages

    def copy_message(event, root):
        root.clipboard_clear()
        root.clipboard_append(event.widget.get("1.0", "end-1c"))

    def display_messages(messages):
        root = tk.Tk()
        root.title("Extracted Messages")

        text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=20)
        text_area.pack(fill="both", expand=True)

        def show_item(item_number):
            # Ensure item number is within valid range
            if 1 <= item_number <= len(messages):
                index = len(messages) - item_number
                message_text = messages[index] + "\n\n"
                text_area.delete("1.0", tk.END)  # Clear text area
                text_area.insert(tk.END, message_text)
                text_area.tag_add("copyable", "end-2l", "end-1c")
                text_area.tag_bind("copyable", "<Button-1>", lambda event: copy_message(event, root))

        # Define keyboard shortcuts
        def show_item_n(event, n):
            if event.modifiers & tk.CONTROL:
                show_item(n)

        # Bind Ctrl+1 to Ctrl+9
        for i in range(1, 10):
            root.bind(f"<Control-{i}>", lambda event, n=i: show_item_n(event, n))

        # Display all messages initially
        for message in messages[::-1]:
            message_text = message + "\n\n"
            text_area.insert(tk.END, message_text)
            text_area.tag_add("copyable", "end-2l", "end-1c")
            text_area.tag_bind("copyable", "<Button-1>", lambda event: copy_message(event, root))

        root.mainloop()

    # Extract messages from file
    messages = extract_messages("clipboard.txt")
    display_messages(messages)

