from tkinter import *

from PIL import Image, ImageTk


def topPanel(self):
    Frame_Top = Frame(self.Mainmenuroot, bg="#343434")
    Frame_Top.place(x=250, y=0, width=self.width, height=60)
    Button(Frame_Top, text="MyProfile", command=self.myprofile, font=("Goudy old style", 15),
           bg="#FFFFFF",
           fg="#F25125").place(x=350, y=10, width=200, height=40)
    image = Image.open("D:\GymSystem\Materials\Photos\Logo.png")
    resize_image = image.resize((60, 60))
    img = ImageTk.PhotoImage(resize_image)
    label1 = Label(Frame_Top, image=img)
    label1.place(x=885, y=0)
    label1.image = img
