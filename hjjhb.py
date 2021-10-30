from tkinter import *
import random

root=Tk()

root.title("Luck Friend Wheel")
root.geometry("500x500")


list1 = ["James", "Isabella", "Sophia", "Oliver", "Peter"]
print(list1)

def random_number():
    random_no = random.randint(0, 4)
    print(random_no)
    random_lucky_friend = list1[random_no]
    print("your Lucky Friend: " + random_lucky_friend)
    
    btn1 = Button(root)
    btn1 = Button(root, text="Who is yoour lucky friend? ", command = random_number)
    btn1.place(relx= 0.5,rely = 0.5, anchor = center)
    
    root.mainloop()