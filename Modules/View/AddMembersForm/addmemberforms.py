from tkinter import *


def AddMemberPanel(self):
    Frame_AddMember = Frame(self.Mainmenuroot, bg="white")
    Frame_AddMember.place(x=250, y=60, width=950, height=950)

    Label(Frame_AddMember, text="Membership Form", font=("Goudy old style", 20, "bold", "underline"), fg="#000000",
          bg="#FFFFFF").place(
        x=345, y=10)
    Label(Frame_AddMember, text="Personal Details :", font=("Goudy old style", 15, "bold", "underline"), fg="#000000",
          bg="#FFFFFF").place(
        x=50, y=50)
    Label(Frame_AddMember, text="Name:", font=("Goudy old style", 12), fg="#000000",
          bg="#FFFFFF").place(
        x=55, y=100)
    self.membername = Entry(Frame_AddMember, font=("Goudy old style", 12),
                            fg="#343434",
                            bg="#FFFFFF")
    self.membername.place(x=150, y=100, width=300)
    Label(Frame_AddMember, text="Address:", font=("Goudy old style", 12), fg="#000000",
          bg="#FFFFFF").place(
        x=55, y=150)
    self.address = Entry(Frame_AddMember, font=("Goudy old style", 12),
                         fg="#343434",
                         bg="#FFFFFF")
    self.address.place(x=150, y=150, width=300)
    Label(Frame_AddMember, text="Mobile No:", font=("Goudy old style", 12), fg="#000000",
          bg="#FFFFFF").place(
        x=55, y=200)
    self.mobileno = Entry(Frame_AddMember, font=("Goudy old style", 12),
                          fg="#343434",
                          bg="#FFFFFF")
    self.mobileno.place(x=150, y=200, width=300)
    Label(Frame_AddMember, text="Email:", font=("Goudy old style", 12), fg="#000000",
          bg="#FFFFFF").place(
        x=500, y=200)
    self.phoneno = Entry(Frame_AddMember, font=("Goudy old style", 12),
                         fg="#343434",
                         bg="#FFFFFF")
    self.phoneno.place(x=600, y=200, width=250)
    Label(Frame_AddMember, text="Age:", font=("Goudy old style", 12), fg="#000000",
          bg="#FFFFFF").place(
        x=55, y=250)
    self.age = Entry(Frame_AddMember, font=("Goudy old style", 12),
                     fg="#343434",
                     bg="#FFFFFF")
    self.age.place(x=150, y=250, width=80)
    Label(Frame_AddMember, text="Gender:", font=("Goudy old style", 12), fg="#000000",
          bg="#FFFFFF").place(
        x=300, y=250)
    options = [
        "Male",
        "Female"
    ]
    self.genderselect = StringVar()
    self.genderselect.set("....")
    self.gender = OptionMenu(Frame_AddMember, self.genderselect, *options)
    self.gender.place(x=370, y=250, width=80)
    self.gender.configure(background="white")
    Label(Frame_AddMember, text="Blood Group:", font=("Goudy old style", 12), fg="#000000",
          bg="#FFFFFF").place(
        x=500, y=250)
    options = [
        "A+",
        "O+",
        "B+",
        "AB+",
        "A-",
        "O-",
        "B-",
        "AB-"
    ]
    self.bloodselect = StringVar()
    self.bloodselect.set("....")
    self.bloodgp = OptionMenu(Frame_AddMember, self.bloodselect, *options)
    self.bloodgp.configure(background="white")
    self.bloodgp.place(x=600, y=250, width=80)
    Label(Frame_AddMember, text="Emergency Contact Person:", font=("Goudy old style", 12), fg="#000000",
          bg="#FFFFFF").place(
        x=55, y=300)
    self.emergencycontactperson = Entry(Frame_AddMember, font=("Goudy old style", 12),
                                        fg="#343434",
                                        bg="#FFFFFF")
    self.emergencycontactperson.place(x=250, y=300, width=200)
    Label(Frame_AddMember, text="Emergency Contact No:", font=("Goudy old style", 12), fg="#000000",
          bg="#FFFFFF").place(
        x=480, y=300)
    self.emergencycontactnumber = Entry(Frame_AddMember, font=("Goudy old style", 12),
                                        fg="#343434",
                                        bg="#FFFFFF")
    self.emergencycontactnumber.place(x=650, y=300, width=200)
    Label(Frame_AddMember, text="Membership Details :", font=("Goudy old style", 15, "bold", "underline"), fg="#000000",
          bg="#FFFFFF").place(
        x=55, y=350)
    self.gym = IntVar()
    Checkbutton(Frame_AddMember, text="Gym", font=("Goudy old style", 15),
                fg="#343434",
                bg="#FFFFFF", variable=self.gym).place(x=55, y=400)
    self.cardio = IntVar()
    Checkbutton(Frame_AddMember, text="Cardio", font=("Goudy old style", 15),
                fg="#343434",
                bg="#FFFFFF", variable=self.cardio).place(x=250, y=400)
    self.onemonth = IntVar()
    Checkbutton(Frame_AddMember, text="One Month", font=("Goudy old style", 15),
                fg="#343434",
                bg="#FFFFFF", variable=self.onemonth).place(x=55, y=450)
    self.threemonth = IntVar()
    Checkbutton(Frame_AddMember, text="Three Months", font=("Goudy old style", 15),
                fg="#343434",
                bg="#FFFFFF", variable=self.threemonth).place(x=250, y=450)
    self.sixmonth = IntVar()
    Checkbutton(Frame_AddMember, text="Six Months", font=("Goudy old style", 15),
                fg="#343434",
                bg="#FFFFFF", variable=self.sixmonth).place(x=450, y=450)
    self.morning = IntVar()
    Checkbutton(Frame_AddMember, text="Morning", font=("Goudy old style", 15),
                fg="#343434",
                bg="#FFFFFF", variable=self.morning).place(x=55, y=500)
    self.evening = IntVar()
    Checkbutton(Frame_AddMember, text="Evening", font=("Goudy old style", 15),
                fg="#343434",
                bg="#FFFFFF", variable=self.evening).place(x=250, y=500)
    Button(Frame_AddMember, text="Next", command=self.inputvalidation, bd=0, font=("Goudy old style", 15),
           bg="#F25125",
           fg="#F9F1F1").place(x=772, y=520, width=80, height=40)
