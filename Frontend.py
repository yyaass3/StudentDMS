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

# Functions
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

# Frames
  mainFrame = frame(self.root, bg = 'cadet blue')
  mainFrame.grid()
  titFrame = frame(mainFrame, bd=2, padx=54, pady=8, bg='ghost white', relief=ridge)
  titFrame.pack(side=TOP)
  self.lblTit = label(titFrame, font=('times new roman', 48, bold),text='Student Database Management System', bg='ghost white')
  self.lblTit.grid()
  buttonFrame = frame(mainFrame, bd=2, width=1350, height=70, padx=19, pady=10, bg='ghost white', relief=ridge)
  buttonFrame.pack(side=bottom)
  dataFrame = frame(mainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=ridge, bg='cadet blue')
  dataFrame.pack(side=bottom)
  dataFrameLeft = labelFrame(dataFrame, bd=1, width=1000, height=600, padx=20, relief=ridge, bg='ghost white', font=('times new roman', 26, 'bold'),text='student info\n')
  dataFrameLeft.pack(side=left)
  dataFrameRight = labelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE,bg="Ghost White",font=('times new roman',20,'bold'),text="Student Details\n")
  dataFrameRight.pack(side=right)

# Entries
  self.lblStdID = label(dataFrameLeft, font=('times new roman', 20, 'bold'), text='student ID: ', padx=2, pady=2, bg='ghost white')
  self.lblStdID.grid(row=0, column=0, sticky=w)
  self.txtStdID = entry(dataFrameLeft, font=('times new roman', 20, 'bold'), textVariable=StdID, width=39)
  self.txtStdID.grid(row=0, column=1)
  
  self.lblfNa = label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="firstName:", padx=2, pady=2,bg="Ghost White")
  self.lblfNa.grid(row=1, column=0, sticky=w)
  self.txtfNa = entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=firstName, width=39)
  self.txtfNa.grid(row=1, column=1)

  self.lblsNa = label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="surName:", padx=2, pady=2,bg="Ghost White")
  self.lblsNa.grid(row=2, column=0, sticky=w)
  self.txtsNa = entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=surName, width=39)
  self.txtsNa.grid(row=2, column=1)

  self.lbldob = label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="dob:", padx=2, pady=2,bg="Ghost White")
  self.lbldob.grid(row=3, column=0, sticky=w)
  self.txtdob = entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=dob, width=39)
  self.txtdob.grid(row=3, column=1)

  self.lblage = label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="age:", padx=2, pady=2,bg="Ghost White")
  self.lblage.grid(row=4, column=0, sticky=w)
  self.txtage = entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=age, width=39)
  self.txtage.grid(row=4, column=1)

  self.lblgender = label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="gender:", padx=2, pady=2,bg="Ghost White")
  self.lblgender.grid(row=5, column=0, sticky=w)
  self.txtgender = entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=gender, width=39)
  self.txtgender.grid(row=5, column=1)

  self.lbladr = label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="address:", padx=2, pady=2,bg="Ghost White")
  self.lbladr.grid(row=6, column=0, sticky=w)
  self.txtadr = entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=address, width=39)
  self.txtadr.grid(row=6, column=1)

  self.lblmobile = label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="mobile:", padx=2, pady=2,bg="Ghost White")
  self.lblmobile.grid(row=7, column=0, sticky=w)
  self.txtmobile = entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=mobile, width=39)
  self.txtmobile.grid(row=7, column=1)

# Scroll bar and list box
  scrollbar = scrollbar(dataFrameRight)
  scrollbar.grid(row=0, column=1, sticky='ns')

  studentList = listbox(dataFrameRight, width=41, height=16, font=('times new roman', 12, 'bold'), yscrollcommand=scrollbar.set)
  studentList.bind('<<listboxselect>>', studentRec)
  studentList.grid(row-0, column=0, padx=8)
  scrollbar.config(command=studentList.yview)

# Buttons
  self.btnaddData = button(buttonframe, text='Add New', font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=addData)
  self.btnaddData.grid(row=0, column=0)

  self.btndisplayData = button(buttonFrame, text='Display', font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=displayData)
  self.btndisplayData.grid(row=0, column=1)

  self.btnclearData = button(buttonFrame, text='Clear', font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=clearData)
  self.btnclearData.grid(row=0, column=2)

  self.btndeleteData = button(buttonFrame, text='Delete', font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=deleteData)
  self.btndeleteData.grid(row=0, column=3)

  self.btnsearchData = button(buttonFrame, text='Search', font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=searchDatabase)
  self.btnsearchData.grid(row=0, column=4)

  self.btnupdateData = button(buttonFrame, text='Update', font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=update)
  self.btnupdateData.grid(row=0, column=5)

  self.btnExit = button(buttonFrame, text='Exit', font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=iExit)
  self.btnExit.grid(row=0, column=6)

if __name__ == '__main__':
  root = tk()
  application = student(root)
  root.mainloop()
