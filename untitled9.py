from tkinter import *
root = Tk()
root.title("Fever Report")
root.geometry("600x600")

question1_radioButton=StringVar(value="0")

Question1=Label(root, text ="Do you have headache and sore throat?")
Question1.pack()
question1_rl1=Radiobutton(root, text = "yes", variable=question1_radioButton, value="yes")
question1_rl1.pack
Question1_r2=Radiobutton(root, text = "no", variable=question1_radioButton, value="no")
Question1_r2.pack

question2_radioButton=StringVar(value="0")

Question2=Label(root, text ="Is you body temperture high?")
Question2.pack()
question2_rl1=Radiobutton(root, text = "yes", variable=question1_radioButton, value="yes")
question2_rl1.pack
Question2_r2=Radiobutton(root, text = "no", variable=question1_radioButton, value="no")
Question2_r2.pack

question3_radioButton=StringVar(value="0")

Question3=Label(root, text ="Are there any symptoms of eye redness?")
Question3.pack()
question3_rl1=Radiobutton(root, text = "yes", variable=question1_radioButton, value="yes")
question3_rl1.pack
Question3_r2=Radiobutton(root, text = "no", variable=question1_radioButton, value="no")
Question3_r2.pack

def fever_score():
    score = 0
    if question1_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question2_radioButton.get()=="yes":
        score = score+20
        print(score)
  
    if question3_radioButton.get()=="yes":
       score = score+20
       print(score)

    if score <= 20:
        messagebox.showinfo("Report","You don't need to visit a doctor.")
    elif  score > 20 and score <= 40:
        messagebox.showinfo("Report","you might perhaps have to visit a doctor.")
    else :
        messagebox.showinfo("Report","I strongly advise you to visit a doctor")
btn = Button(root, text= "click me", command = fever_score)        
btn.pack
root.mainloop