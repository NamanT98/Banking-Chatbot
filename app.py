from speech2text import *
import tkinter as tk

device=0

root = tk.Tk()
button_rec = tk.Button(root, text='Start', command=start)
button_rec.pack()
button_stop = tk.Button(root, text='Stop', command=stop)
button_stop.pack()


root.mainloop() 