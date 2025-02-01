import  tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except Exception as e:
              messagebox.showerror("Error","Invalid Input")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + button_text)
    
#Create the main window
root = tk.Tk()
root.title("Simple Calculator")

entry_var = tk.StringVar()
entry = tk.Entry(root,textvariable=entry_var,font=("Arial",18),justify="right")
entry.grid(row=0,column=0,columnspan=4,ipadx=8,ipady=8)

buttons = [
    ('7','8','9','/'),
    ('4','5','6','*'),
    ('1','2','3','-'),
    ('C','0','=','+')
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        button = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: on_click(t))
        button.grid(row=i+1, column=j, ipadx=10, ipady=10, padx=5, pady=5)

root.mainloop()