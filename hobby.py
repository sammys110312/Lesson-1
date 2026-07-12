import tkinter as tk

window = tk.Tk()
window.title("My Profile Card")
window.geometry('400x300')

heading = tk.Label(
    window,
    text = "Profile Card: ",
    bg = "purple",
    fg =  "white",
    font = ("Arial", 16, "bold")
)

heading.grid(row=0, column=0, columnspan=2, sticky="ew", pady = 10)

name_label = tk.Label(window , text = "Name: ")
name_label.grid(row=1, column=0, padx=10, pady=5, sticky = "w")

name_entry = tk.Entry(window , width = 30)
name_entry.grid(row=1, column =1, padx=10, pady=10)

hobby_label = tk.Label(window , text = "Hobby: ")
hobby_label.grid(row=2, column=0, padx=10, pady = 5, sticky = "w")

hobby_entry = tk.Entry(window , width = 30)
hobby_entry.grid(row=2, column =1, padx=10, pady=5)

about_me = tk.Label(window, text = "About Me: ")
about_me.grid(
    row = 3,
    column  = 0,
    columnspan = 2,
    padx = 10,
    pady = 5,
    sticky = "nw"
)
frame = tk.Frame(window, bd = 2, relief = "solid")
frame.grid(row=3, column=1, padx=10, pady=5)
about_text = tk.Text(frame, width =25, height = 6)
about_text.pack()

def show_card():
    name = name_entry.get()
    hobby = hobby_entry.get()
    about = about_text.get("1.0","end")
    print(name)
    print(hobby)
    print(about)

save_button = tk.Button(window,text = "Show My Card", command = show_card)
save_button.grid(row=4, column=0, columnspan=2, pady=15)
window.mainloop()