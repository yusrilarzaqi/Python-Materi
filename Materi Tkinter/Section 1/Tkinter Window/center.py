import tkinter as tk
from types import LambdaType

root = tk.Tk()
root.title("Tkinter Window - Center")

window_width = 300
window_height = 200

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

x = tk.Label(root, text=f"{center_x} {center_y}")
x.pack()

y = tk.Label(root, text=f"{screen_width} {screen_height}")
y.pack()

root.mainloop()
