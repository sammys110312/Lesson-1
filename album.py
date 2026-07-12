from tkinter import *

from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title("FIFA WORLD CUP ALBUM")
root.geometry("500x500")
image = Image.open("photo.jpg")
image = image.resize((250,250))
photo = ImageTk.PhotoImage(image)
image_label = Label(root,image=photo)
image_label.pack(pady = 10)

def show_message():
    messagebox.showinfo("Image Loaded", "The Photo Has Been Loaded Successfully")
def open_details():
    top = Toplevel(root)
    top.title("Photo Details")
    top.geometry("300x200")
    Label(top, text = "Photo Name: photo.jpg").pack(pady = 5)
    Label(top, text = f"Height: {image.height}").pack()
    Label(top, text = "Format - JPG").pack()

Button(
    root,
    text = "Show Message",
    command = show_message
).pack(pady = 10)

Button(
    root,
    text = "Phot Details",
    command = open_details
).pack()

root.mainloop()