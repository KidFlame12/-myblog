from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.minsize(650,650)
root.maxsize(650,650)

open_img = ImageTk.PhotoImage(Image.open ("open.png"))
save_img = ImageTk.PhotoImage(Image.open ("save.png"))
exit_img = ImageTk.PhotoImage(Image.open ("exit.png"))


label_file_name = Label(root, text="file name")
label_file_name.place(relx=0.28,rely=0.03,anchor= CENTER)

input_file_name = Entry(root)
input_fil_name.place(relx=0.46,rely=0.03,anchor= CENTER)


my_text= Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor= CENTER)

open_button=Button(root,image=open_img,text="OpenFile", command=openFile)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)

def addData():
    Input_file_name.insert(END,"myfile")
    
def clearInputFeild():
    input_file_name.delete(0, END)
    
def clearTextarea():
    my_text.delete(1.0, END)
    
