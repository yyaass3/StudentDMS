# Frontend
from tkinter import *
import tkinter.messagebox
import StudentDMS

class student:

  def __init__(self, root):
    self.root = root
    self.root.title('Student Database Management System')
    self.root.geometry('1350x750+0+0')
    self.root.config(bg='cadet blue')

    StdID = stringvar()
    firstName = stringvar()
    surName = stringvar()
    dob = stringvar()
    age = stringvar()
    gender = stringvar()
    address = stringvar()
    mobile = stringvar()

  def iExit():
    iExit = tkinter.messagebox.askyesno("Student Database Management Systems", "Confirm if you want to exit")
    if iExit >0 :
      root.destroy()
      return

  def clearData():
    self.txtStdID.delete(0, END)
    self.txtfNa.delete(0, END)
    self.txtsNa.delete(0, END)
    self.txtdob.delete(0, END) 
    self.txtage.delete(0, END)
    self.txtgender.delete(0, END)
    self.txtadr.delete(0, END)
    self.txtmobile.delete(0, END)

  def addData():
    if(len(StdID.get()))!= 0:
      StudentDMS.addStdRec(StdID.get(), firstName.get(), surName.get(), dob.get(), age.get(), gender.get(), address.get(), mobile.get())
      studentList.delete(0, END)
      studentList.insert(END, (StdID.get(), firstName.get(), surName.get(), dob.get(), age.get(), gender.get(), address.get(), mobile.get()))

  def DisplayData():
    studentList.delete(0, END)
    for rows in StudentDMS.viewData():
      studentList.insert(END, rows, str(''))

  def StudentRec(event):
    global sd
    searchSd = studentList.curselection()[0]
    sd = studentList.get(searchSd)

    self.txtSdtID.delete(0, END)
    self.txtSdtID.insert(END, sd[1])
    self.txtfNa.delete(0, END)
    self.txtfNa.insert(END, sd[2])
    self.txtsNa.delete(0, END)
    self.txtsNa.insert(END, sd[3])
    self.txtdob.delete(0, END)
    self.txtdob.insert(END, sd[4])
    self.txtage.delete(0, END)
    self.txtage.insert(END, sd[5])
    self.txtgender.delete(0, END)
    self.txtgender.insert(END, sd[6])
    self.txtadr.delete(0, END)
    self.txtadr.insert(END, sd[7])
    self.txtmobile.delete(0, END)
    self.txtmobile.insert(END, sd[8])

  def deleteData():
    if len(StdID.get()) != 0 :
      StudentDMS.deleteRec(sd[0])
      clearData()
      DisplayData()

  def searchDatabase():
    studentList.delete(0, END)
    for rows in StudentDMS.searchData(StdID.get(), firstName.get(), surName.get(), dob.get(), age.get(), gender.get(), address.get(), mobile.get()):
      studentList.insert(END, rows, str(''))
  
  def update():
    if len(StdID.get()) != 0:
      StudentDMS.deleteRec(sd[0])
    if len(StdID.get()) != 0:
      StudentDMS.addStdRec(StdID.get(), firstName.get(), surName.get(), dob.get(), age.get(), gender.get(), address.get(), mobile.get())
      studentList.delete(0, END)
      studentList.insert(END, (StdID.get(), firstName.get(), surName.get(), dob.get(), age.get(), gender.get(), address.get(), mobile.get()))
