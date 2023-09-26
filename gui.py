import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Small GUI Window")

    # Set the width and height of the window
    window_width = 300
    window_height = 200

    # Calculate the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Set the window size and position
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Disable window resizing
    root.resizable(False, False)

    # Create a label widget
    label = tk.Label(root, text="This is a small window.")
    label.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
