from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
root.Tk()
root.title("Resturant order")
root.geometry("900x500")
#-----------------Burger_Image----------
burger = ImageTk.PhotoImage(Image.open ("burger1.png"))
burger_image=Label(root)
burger_image["image"]=burger
burger_image.place(relx=0.7, rely=0.5,anchor=CENTER)
label_heading=Label(root,text="Arnolds", font=("times",40,"bold"), fg="Orange")
label_heading.place(relx=0.06, rely=0.2,anchor=CENTER)
label_select_dish=Label(root,text="Select Dish",font=("times",15))
label_select_dish.place(relx=0.06, rely=0.2,anchor=CENTER)
dish=["burger","iced_americano"]
dish_dropdown = ttk.Combobox(root ,state = "read only",values = dish)
dish_dropdown.place(relx=0.25, rely=0.2, anchor=CENTER)
label_select_addons=Label(root,text="Select Add-ons",font="times",15)
label_select_addons.place(relx=0.08, rely=0.5,anchor=CENTER)
toppings=[]
toppings_dropdown = ttk.Combobox(root,state = "read only",values = dish)
dish__amount=Label(root,font=("times",15,"bold"))
dish_amount.place(relx=0.2,rely=0.75,anchor=CENTER)
class parent():
    
    def __init__(self):
        print("This is parent")
        
    def menu(dish):
        if dish=="burger":
            toppings=["cheese","jalapeno"]
            toppings
            print("you can add the following toppings")
            print("More cheese | Add jalapeno")
        elif dish=="iced_americano":
            print("you can add the following toppings")
            print("Add` chocolate flavor | Add caramel flavor")
        else:
            print("please enter valid dish")
            
    def final_amount(dish, add_on):
        if dish=="burger" and add_ons=="cheese":
            print("you total $25.25")
        elif dish=="burger" and add_ons=="jalepeno":
            print("your total is $27.85")
        elif dish=="iced_americano" and add_ons=="chocolate":
            print("your total is $15.49")
        elif dish=="iced_americano" and add_ons=="caramel":
            print("your total is 17.96")
            
class child1(parent):
    
    def __init__(self,dish):
        self.new_wish = dish
    def get_menu(self):
       parent.menu(self.new_dish)

class child2(parent):
    
    def __init__(self,dish,addons):
        self.newdish = dish
        self.addons = addons
        
    def get_final_amount(self):
        parent.final_amount(self.new_dish,self.addons)
        
child1_object=child1("burger")
child1_object.getmenu()

child2_object=child2("burger","jalepeno")
child2_object.get_final_amount()
