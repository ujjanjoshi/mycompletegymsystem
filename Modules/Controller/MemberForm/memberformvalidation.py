from tkinter import messagebox

from Modules.View.AddMembersForm.addpaymentdetials import AddMemberPaymentPanel


def memberformvalidation(self):
    self.dateto = "Choose date"
    self.datefrom = "Choose date"
    self.membersfullname = self.membername.get().title()
    self.memberadress = self.address.get().title()
    self.membermobileno = self.mobileno.get()
    self.memberphonene = self.phoneno.get()
    self.membeberage = self.age.get()
    self.membergender = self.genderselect.get()
    self.memberbloodgroup = self.bloodselect.get()
    self.memberemergencycontactperson = self.emergencycontactperson.get()
    self.memberemergencycontactnumber = self.emergencycontactnumber.get()
    self.memberchoosegym_cardio = ""
    self.memberchoosemonths = ""
    self.memberchooseshift = ""
    if (self.memberphonene == ""):
        self.memberphonene = "-"
    if (self.memberbloodgroup == "...."):
        self.memberbloodgroup = "-"
    if (self.memberemergencycontactnumber == ""):
        self.memberemergencycontactnumber = "-"
    if (self.memberemergencycontactperson == ""):
        self.memberemergencycontactperson = "-"
    # gym+cardio option
    if (self.gym.get() == 1 and self.cardio.get() == 0):
        self.memberchoosegym_cardio = "Gym"
    else:
        self.memberchoosegym_cardio = "Gym+Cardio"

    # month option
    if (self.onemonth.get() == 1):
        self.memberchoosemonths = "1month"
    elif (self.threemonth.get() == 1):
        self.memberchoosemonths = "3months"
    else:
        self.memberchoosemonths = "6months"

    # shift option
    if (self.morning.get() == 1):
        self.memberchooseshift = "Morning"
    else:
        self.memberchooseshift = "Evening"
    # other validation
    if (self.membersfullname == "" or self.memberadress == "" or self.membermobileno == "" or
            self.membeberage == "" or self.membergender == "" or self.phoneno == ""):
        messagebox.showerror("Error", "Fill Required Information for Personal Details")
    elif (
            self.gym.get() == 0 and self.cardio.get() == 0 and self.onemonth.get() == 0 and self.threemonth.get() == 0 and self.sixmonth.get() == 0
            and self.morning.get() == 0 and self.evening.get() == 0):
        messagebox.showerror("Error", "Fill Required Information for Membership Details")
    else:
        AddMemberPaymentPanel(self)
