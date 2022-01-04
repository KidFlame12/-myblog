from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk


root = Tk()
root.title("Planet ENcyclopedia")
root.geometry("500x500")
root.configure(background="lightblue")

Mercury = ImageTk.PhotoImage(Image.open ("mercury.jpeg"))
Venus = ImageTk.PhotoImage(Image.open ("venus.jpeg"))
Earth = ImageTk.PhotoImage(Image.open ("earth.jpeg"))

label_planet = Label(root, text="Planet : ", bg="lightblue")
label_planet_name = Label(root,font=("courier",18,"bold"),bg="lightblue")
label_planet_image = Label(root, bg="gold2", highlightthinkness=5, boderwidth=2,relief=SOLID)
label_planet_gravity_radius = Label(root,font("castellar"), bg="lightblue")
label_planet_info = Label(root,font=("couurier",10,"bold"), bg="lightblue",wraplength=500)

planets = ["Mercury","Venus", "Earth"]
selectedval = StringVar()
dropdown = ttk.Combobox(root, values = planets, textvariable=selectedval)

def Planetinfo():
   btn = Button(root, text="Show Plant Info" , command=PlanetInfo)   
btn.place(relx=0.5, rely=0.18, anchor=CENTER)

label_planet.place(relx=0.2, rely=0.1 , anchor=CENTER)
label_planet_name.place(relx=0.5, rely=0.25, anchor=CENTER)
label_planet_image.place(relx=0.5, rely=0.5, anchor=CENTER)
label_planet_gravity_radius(relx=0.5, rely=0.8, anchor=CENTER)
label_planet_info.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()