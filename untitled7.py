from tkinter import *
root=Tk()
root.title("Mutiplication Master")
root.geometry("600x400")
input_box = Entry(root)
input_box.pack()


def addition():
    number = 9
    get_input = input_box.get()
    try:
        print(number + get_input)
    except(TypeError):    
        messagebox.showinfo("Error", "Cannot add two different data types: integer and string")
Button = Button(root , text= "multply", command = multiplication)
button.pack()
root.mainloop