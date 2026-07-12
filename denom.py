from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Denomination Calculator")
root.geometry("350x250")

def calculate():
    amount = int(entry.get())

    note1000 = amount // 1000
    amount = amount % 1000

    note500 = amount // 500
    amount = amount % 500

    note200 = amount // 200
    amount = amount % 200

    label1000.config(text = "£1000 notes: " + str(note1000))
    label500.config(text = "£500 notes: " + str(note500))
    label200.config(text = "£200 notes: " + str(note200))

    messagebox.showinfo("Success", "Calculation Completed")

heading = Label(root, text = "Denomination Calculator", font = ("Arial", 16, "bold"))
heading.pack(pady = 10)
Label(root, text = "Enter Amount").pack()
entry = Entry(root)
entry.pack()

button = Button(root, text = "Calculate", command = calculate).pack(pady = 10)

label1000 = Label(root, text = "£1000 notes: 0")
label1000.pack()

label500 = Label(root, text = "£500 notes: 0")
label500.pack()

label200 = Label(root, text = "£200 notes: 0")
label200.pack()

root.mainloop()