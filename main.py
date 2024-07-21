from read_clipboard import read_clipboard_history

import clipboard

def main():
    clipboard_history = []

    history = clipboard.store_clipboard(clipboard_history)
    print(history)
    
    clipboard_history = read_clipboard_history()  # Call the function
    print("Clipboard History:")
    for item in clipboard_history:
        print(item)

    

if __name__ == '__main__':
    main()


