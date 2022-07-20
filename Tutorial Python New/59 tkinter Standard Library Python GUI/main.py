# GUI -> Graphical User Interface

from tkinter.messagebox import showinfo
from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.configure(background="#dfdfdf")
root.geometry("300x200")
root.resizable(False, False)
root.title("HELLO WORLD")

# Constant Variable
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# frame input
input_frame = ttk.Frame(root)
# penempatan (grid, pack, place)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# komponen-komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame, text="NAMA DEPAN : ")
nama_depan_label.pack(padx=10, pady=0, fill="x", expand=True)
# 2. Entry nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, pady=10, fill="x", expand=True)
# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="NAMA BELAKANG : ")
nama_belakang_label.pack(padx=10, pady=0, fill="x", expand=True)
# 4. Entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, pady=10, fill="x", expand=True)
# 5. Tombol
def tombol_click():
    """FUNGSI INI AKAN DI EXEKSI SAAT BUTTON DITEKAN"""
    result = f"{NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}"
    print(result)
    showinfo(title="NAMAKU", message=result)


button_enter = ttk.Button(input_frame, text="ENTER", command=tombol_click)
button_enter.pack(padx=10, pady=10, fill="x", expand=True)


## MAIN LOOP WINDOW
root.mainloop()
