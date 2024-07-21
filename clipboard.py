import pyperclip

def store_clipboard(filename="clipboard.txt"):
  """Stores clipboard content in a file, maintaining a maximum of 9 lines."""

  try:
    with open(filename, "r") as f:
      history = f.readlines()
  except FileNotFoundError:
    history = []

  text = pyperclip.paste()
  if not history or text != history[-1]:
    history.append(text + "\n")
    if len(history) > 9:
      history.pop(0)

  with open(filename, "w") as f:
    f.writelines(history)

  return history
