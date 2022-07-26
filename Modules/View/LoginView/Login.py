from tkinter import *
from tkinter import messagebox

from Modules.Controller.login.loginvalidation import LoginValidation
from Modules.Controller.login.returnloginname import ReturnName
from Modules.View.MainMenu.mainmenu import MainPage


class LoginSys:
    def __init__(self, login_main_root):
        self.login_main_root = login_main_root
        self.login_main_root.title("LOGIN")
        self.width = "1199"
        self.height = "650"
        self.usr = ""
        self.login_main_root.geometry(self.width + "x" + self.height + "+100+30")
        self.login_main_root.resizable(False, False)
        self.left()
        self.right()

    def left(self):
        global photo
        Frame_left = Frame(self.login_main_root, bg="#FFFFFF")
        Frame_left.place(x=0, y=0, width=(int(self.width) / 2), height=int(self.height))
        photo = PhotoImage(file="D:\GymSystem\Materials\Photos\logo.png")
        varun_label = Label(image=photo, background="#FFFFFF").place(x=0, y=0, width=(int(self.width) / 2),
                                                                     height=int(self.height))

    def right(self):
        global photo
        Frame_Right = Frame(self.login_main_root, bg="#F98C6E")
        Frame_Right.place(x=(int(self.width) / 2), y=0, width=(int(self.width) / 2), height=int(self.height))
        Frame_Login = Frame(Frame_Right, bg="#FFFFFF")
        Frame_Login.place(x=110, y=110, width=390, height=450)
        Label(Frame_Login, text="Login", font=("Goudy old style", 20, "bold"), fg="black", bg="#FFFFFF").place(x=165,
                                                                                                               y=30)
        Label(Frame_Login, text="Username:", font=("Goudy old style", 15, "bold"), fg="black", bg="#FFFFFF").place(x=30,
                                                                                                                   y=140)
        self.username = Entry(Frame_Login, font=("Goudy old style", 15), bg="#FFF9F9", highlightcolor="#EA7676",
                              highlightbackground="#EA7676", highlightthickness=1)
        self.username.place(x=140, y=140, width=200, height=30)
        Label(Frame_Login, text="Password:", font=("Goudy old style", 15, "bold"), fg="black", bg="#FFFFFF").place(x=30,
                                                                                                                   y=240)
        self.password = Entry(Frame_Login, font=("Goudy old style", 15), show="*", bg="#FFF9F9",
                              highlightcolor="#EA7676",
                              highlightbackground="#EA7676", highlightthickness=1)
        self.password.place(x=140, y=240, width=200, height=30)
        Button(Frame_Login, text="Login", command=self.Loginbtn, bd=0, font=("Goudy old style", 15),
               bg="#F25125",
               fg="#F9F1F1").place(x=110, y=360, width=200, height=40)

    def Loginbtn(self):
        logins = LoginValidation(self.username.get(), self.password.get())
        if (logins == 1):
            name = ReturnName(self.username.get())
            usr = self.username.get().upper()
            self.close_windowlogin()
            MainPage(Tk(), usr, name)
        else:
            messagebox.showerror("Error", "Login Error!!")

    def close_windowlogin(self):
        self.login_main_root.destroy()
