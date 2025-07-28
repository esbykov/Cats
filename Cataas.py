from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

window = Tk()
window.title("Cats!")
window.geometry("600x400")

label =Label()
label.pack()

url = "https://cataas.com/cat"
img = load_img(url)

if img:
    label.config(image=img)
    label.image = img

window.mainloop()

