import pyperclip
import os

def write_paste(max_items=9):
    clipboard_text = pyperclip.paste()

    try:
        with open("clipboard.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    # Remove empty lines and "Start" and "UniqueEndMsgLOL" markers
    lines = [line.strip() for line in lines if line.strip() and not line.startswith(("Start", "UniqueEndMsgLOL"))]

    # Append new text if it's not already in the list
    if clipboard_text not in lines:
        lines.append(clipboard_text)

    # Limit to max_items
    if len(lines) > max_items:
        lines = lines[-max_items:]

    # Add item numbering
    numbered_lines = [f"Item {i+1}: {line}" for i, line in enumerate(lines)]

    with open("clipboard.txt", "w") as file:
        for line in numbered_lines:
            file.write(f"Start\n{line}\nUniqueEndMsgLOL\n\n")