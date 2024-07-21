import tkinter as tk

class ClipboardGUI:
  def __init__(self, root):
    self.root = root
    self.root.title("Clipboard Manager")

    self.text_widget = tk.Text(root)
    self.text_widget.pack(fill="both", expand=True)

  def update_display(self, history):
    self.text_widget.delete(1.0, tk.END)
    for item in history:
      self.text_widget.insert(tk.END, item + "\n")

# Example usage (assuming a function to call from main.py)
def create_gui(history):
  root = tk.Tk()
  gui = ClipboardGUI(root)
  gui.update_display(history)
  return root, gui
