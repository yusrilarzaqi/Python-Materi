import tkinter as tk

root = tk.Tk()
root.title("TKinter Fixed window")
root.geometry("600x400+50+50")

root.minsize(0, 0)
root.maxsize(600, 400)
# root.resizable(False, False)

root.mainloop()
