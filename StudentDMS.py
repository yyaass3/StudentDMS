# Backend
import sqlite3

# create student table
def StudentData():
  con = sqlite3.connect('student.db')
  cur = con.cursor()
  cur.execute('create table if not exists student(id int primary key, StdID text, firstName text, surName text, dob text, age text, gender text, address text, mobile text);')
  con.commit()
  con.close()

# add data to the table
def addStdRec(StdID, firstName, surName, dob, age, gender, address, mobile):
  con = sqlite3.connet('student.db')
  cur = con.cursor()
  cur.execute('insert into student values(null, ?, ?, ?, ?, ?, ?, ?, ?);', (StdID, firstName, surName, dob, age, gender, address, mobile))
  con.commit()
  con.close()

# view table's data
def viewData():
  con = sqlite3.connect('student.db')
  cur = con.cursor()
  cur.execute('select * from student;')
  rows = con.fetchall()
  con.close()
  return rows

# deleting Data
def deleteRec(id):
  con = sqlite3.connect('student.db')
  cur = con.cursor()
  cur.execute('delete from student where id = ?',(id,))
  con.commit()
  con.close()

# searching Data
def searchData(StdID='', firstName='', surName='', dob='', age='', gender='', address='', mobile=''):
  con = sqlite3.connect('student.db')
  cur = con.cursor()
  cur.execute('select * from student where StdID=? or firstName=? or surName=? or dob=? or age=? or gender=? or address=? or mobile=?;'
,(StdID, firstName, surName, dob, age, gender, address, mobile))
  rows = cur.fetchall()
  con.close()
  return rows

# updating Data
def dataUpdate(id, StdID='', firstName='', surName='', dob='', age='', gender='', address='', mobile=''):
  con = sqlite3.connect('student.db')
  cur = con.cursor()
  cur.execute('update student set (StdID=?, firstName=?, surName=?, dob=?, age=?, gender=?, address=?, mobile=? where id=?;'
,(StdID, firstName, surName, dob, age, gender, address, mobile, id))
  con.commit()
  con.close()

studentData()
