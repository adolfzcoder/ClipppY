def read_clipboard_history(filename="clipboard.txt"):
  """Reads clipboard history from a file and returns a list."""

  try:
    with open(filename, "r") as f:
      history = f.readlines()
  except FileNotFoundError:
    history = []

  # Remove trailing newlines from each line
  history = [line.rstrip("\n") for line in history]

  print(history)

  return history
read_clipboard_history("clipboard.txt")