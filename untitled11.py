from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title("Working On Canvas Using Functions")
root.geometry("600x600")


color_label.place(relx=0.8,rely=0.9, anchor=CENTER)
color_label.place(relx=0.6,rely=0.9, anchor=CENTER)

input_box = Entry(root)
input_box.insert(0,"black")
input_box.place(relx=0.8,rely=0.9, anchor= CENTER)



canvas=Canvas(root, width = 590, height=510, bg = "white", highlightbackground="lightgray")
canvas.pack()



root.mainloop()
    