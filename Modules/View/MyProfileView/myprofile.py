from tkinter import *

from Modules.Controller.MyProfile.Myprofileinfofetch import infofetch


def ProfilePanel(self):
    Frame_profile = Frame(self.Mainmenuroot, bg="white")
    Frame_profile.place(x=250, y=60, width=950, height=950)
    Label(Frame_profile, text="Profile", font=("Goudy old style", 20, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=410, y=10)
    Label(Frame_profile, text="Rv_Id :", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=80, y=80)
    Label(Frame_profile, text="Name :", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=80, y=130)
    Label(Frame_profile, text="Username :", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=80, y=180)
    Label(Frame_profile, text="Address :", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=80, y=230)
    Label(Frame_profile, text="Email :", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=80, y=280)
    Label(Frame_profile, text="Phone_No :", font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=80, y=330)
    infodetailslst = infofetch(self.usr)
    Label(Frame_profile, text="00" + infodetailslst[0], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=410, y=80)
    Label(Frame_profile, text=infodetailslst[1], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=410, y=130)
    Label(Frame_profile, text=infodetailslst[2], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=410, y=180)
    Label(Frame_profile, text=infodetailslst[3], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=410, y=230)
    Label(Frame_profile, text=infodetailslst[4], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=410, y=280)
    Label(Frame_profile, text=infodetailslst[5], font=("Goudy old style", 15, "bold"), fg="#343434",
          bg="#FFFFFF").place(
        x=410, y=330)