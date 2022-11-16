import tkinter as tk
import random as r
sequence=[1,2,3,4,5,5,5,5,5,6]

def func(str1,num):
    print(str1,num)
def start():
    print("MENU")
    print("1. A Normal Dice")
    print("2. A Biased Dice")
    str2=int(input(("Enter your choice(1 or 2)")))
    if str2==1:
        root = tk.Tk()
        root.title("Welcome To Dice Simulator!")
        root.geometry("350x125")
        root.config(bg='#4FA095')
        btn = tk.Button(root, text="Click to roll!", command=lambda: func("The dice rolled=>",num=r.randint(1,6)))
        btn.pack()
        root.after(5000,lambda:root.destroy())
        root.mainloop()
    elif str2==2:
        root = tk.Tk()
        root.title("Welcome To Dice Simulator!")
        root.geometry("350x125")
        root.config(bg='#4FA095')
        btn = tk.Button(root, text="Click to roll!", command=lambda: func("The dice rolled=>",num=r.choice(sequence)))
        btn.pack()
        root.after(4000,lambda:root.destroy())
        root.mainloop()
start()
print("Would you like to Restart or Quit(r/q)")
str3=input("Enter your answer")
if str3=="r":
    start()
else:
    quit()

