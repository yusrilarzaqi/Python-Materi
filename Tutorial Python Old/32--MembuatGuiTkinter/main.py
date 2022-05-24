import tkinter

root=tkinter.Tk()

def event_click():
   label2=tkinter.Label(root,text="Saya tertekan !")
   label2.pack()

label=tkinter.Label(root,text="Ini adalah GUI sederhana yang dibuat oleh python")
tombol=tkinter.Button(root,text="TEKAN !!!",command=event_click)


label.pack()
tombol.pack()

root.mainloop()