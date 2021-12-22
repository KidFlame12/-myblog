from tkinter import *

root = Tk()
root.geometry("500x400")
             
dictionary = {"fruit":"mango",
         "color":"pink",
         "bird":"sparrow"}

try:
    print(dictionary["animal"])
except(KeyError):
    print("key animal is not present in dictionary")