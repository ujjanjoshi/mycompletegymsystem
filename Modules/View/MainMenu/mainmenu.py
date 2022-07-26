from tkinter import *

from Modules.Controller.Attendence.getmemberdetailstodisplay import showmemberattendence
from Modules.Controller.Attendence.presentmembers import presentmembers
from Modules.Controller.Email.sendemail import sendmail
from Modules.Controller.MemberForm.getallinfo import GetfullInfo
from Modules.Controller.MemberForm.getdatefromofmember import getdatefrommember
from Modules.Controller.MemberForm.getdatetoofmember import getdatetomember
from Modules.Controller.MemberForm.memberformvalidation import memberformvalidation
from Modules.Controller.SearchDetials.searchmember import SearchMember
from Modules.Controller.SearchDetials.searchmemberdetails import SerchMemberDetials
from Modules.Controller.ShowUpdatePayment.UpdatePayment import UpdatePayments
from Modules.Controller.ShowUpdatePayment.Updatepaymentindb import updateintodb
from Modules.Controller.ShowUpdatePayment.getdatefromofmember import updategetdatefrommember
from Modules.Controller.ShowUpdatePayment.getdatetoofmember import updategetdatetomember
from Modules.Controller.Updateafterabsent.Updatepaymentindb import updateintodbss
from Modules.Controller.Updateafterabsent.getdatefromofmember import updategetdatefrommemberabsnt
from Modules.Controller.Updateafterabsent.getdatetoofmember import updategetdatetomemberabsnt
from Modules.View.UpdatePaymentAbsnt.UpdatePaymentAbsnt import UpdatePaymentAfterAbsent
from Modules.Controller.Updatedeactivate.updatedeactivate import deactivatemember
from Modules.Controller.showmemberdetials.getmemberdetailstodisplay import showmemberinfo
from Modules.Controller.showmemberdetials.memberdelete import memberdelete
from Modules.View.AddMembersForm.addmemberforms import AddMemberPanel
from Modules.View.AddMembersForm.addpaymentdetials import AddMemberPaymentPanel
from Modules.View.Attendence.attendence import AttendencePanel
from Modules.View.DashboardView.Dashboard import DashBoardPanel
from Modules.View.MainMenu.mainmenuleft import leftPanel
from Modules.View.MainMenu.mainmenushowtime import timeloop
from Modules.View.MainMenu.mainmenutop import topPanel
from Modules.View.MyProfileView.myprofile import ProfilePanel
from Modules.View.ShowMemberdetails.showmembersdetials import MemeberViewDetailsPanel
from Modules.View.ShowMemberdetails.viewfulldetials import fulldetails
from Modules.View.ShowPaymentUpdate.paymnettop import PaymentPanel



class MainPage:
    def __init__(self, Mainmenuroot, usr, name):
        Mainmenuroot.after(0, Mainmenuroot.deiconify)
        self.name = name
        self.usr = usr
        self.dateto = "Choose date"
        self.datefrom = "Choose date"
        self.updatedateto = "Choose date"
        self.updatedatefrom = "Choose date"
        self.updatedatefromabsnt= "Choose date"
        self.updatedatetoabsnt = "Choose date"
        self.Mainmenuroot = Mainmenuroot
        self.Mainmenuroot.title("Main")
        self.width = "1199"
        self.height = "650"
        self.mbmrid = ""
        self.lst=[]
        self.count=-1
        self.Mainmenuroot.geometry(self.width + "x" + self.height + "+100+30")
        self.Mainmenuroot.resizable(False, False)
        self.a = 0
        self.month = ""
        self.left()
        self.top()
        self.deactivembr()
        self.sendmain()
        self.dashboard()


    def left(self):
        leftPanel(self)

    def time(self):
        timeloop(self)

    def top(self):
        topPanel(self)

    def dashboard(self):
        DashBoardPanel(self)

    def logout(self):
        self.close_window_mainmenu()
        from Modules.View.LoginView.Login import LoginSys
        LoginSys(Tk())

    def myprofile(self):
        ProfilePanel(self)

    def addmembers(self):
        AddMemberPanel(self)

    def inputvalidation(self):
        memberformvalidation(self)

    def addpaymentdetails(self):
        AddMemberPaymentPanel(self)

    def getdatefrom(self):
        getdatefrommember(self)

    def getdateto(self):
        getdatetomember(self)

    def getmemberinfo(self):
        GetfullInfo(self)

    def showmemberdetails(self):
        MemeberViewDetailsPanel(self)

    def showmemberinformation(self, monthsss):
        showmemberinfo(self, 1, self.monthss.get(), self.shiftss.get())

    def fulldetailss(self, num):
        fulldetails(self, num)
    def sendmain(self):
        sendmail(self)
    def delete(self, num):
        memberdelete(self, num)

    def paymentdetials(self):
        PaymentPanel(self)

    def updtepayment(self, num):
        UpdatePayments(self, num)

    def updatedb(self):
        updateintodb(self)

    def updategetdatefrom(self):
        updategetdatefrommember(self)

    def updategetdateto(self):
        updategetdatetomember(self)

    def attendnce(self):
        AttendencePanel(self)

    def showattendence(self, monthsss):
        showmemberattendence(self, 1, self.shiftsss.get())

    def presentmemberss(self, num):
        presentmembers(self, num)

    def deactivembr(self):
        deactivatemember(self)

    def makesearch(self,event):
        SearchMember(self,event)
        SerchMemberDetials(self,self.lst)
    def updateaftrasbnt(self,num):
        UpdatePaymentAfterAbsent(self, num)

    def updatedbs(self):
        updateintodbss(self)
    def updategetdatefromabsnts(self):
        updategetdatefrommemberabsnt(self)

    def updategetdatetoabsnts(self):
        updategetdatetomemberabsnt(self)

    def close_window_mainmenu(self):
        self.Mainmenuroot.destroy()


