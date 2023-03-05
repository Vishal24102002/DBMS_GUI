try:
  import mysql-connector
  import tkinter as tk
  from tkinter import messagebox
except:
  import pip
  pip.main(['install','tk'])
  pip.main(['install','mysql-connector'])
  import mysql-connector
  import tkinter as tk
  from tkinter import messagebox

def speak(text):
    engine=pt.init()
    engine.say(text)
    Voices=engine.getProperty('voices') 
    print(Voices) 
    engine.setProperty('voice',Voices[0].id) 
    engine.runAndWait()

def connect():
  mydb=mysql.connector.connect(host="localhost",user="root",password="vishal")
  mycursor=mydb.cursor()
  try:
    mycursor.execute("use aravalian")
  except:
    mycursor.execute("create database aravalian")
    mycursor.execute("use aravalian")
    print("connected successfully")
    speak("connected successfully")
  Start_label.destroy()
  connection_button.destroy()

def main():
  name_label=label(pradeep,text="teacher-name",fg="white",font=('calibre',10,'normal'))
  name_entry=Entry(pradeep,textvariable=user,font=('calibre',10,'normal'))
  id_label=label(pradeep,text="Employee-ID",fg="white",font=('calibre',10,'normal'))
  id_entry=Entry(pradeep,textvariable=ID,font=('calibre',10,'normal'))
  name_label.grid(row=0,column=0)
  name_entry.grid(row=0,column=1)
  id_label.grid(row=1,column=0)
  id_entry.grid(row=1,column=1)
  search_button=Button(pradeep,text="Search",cursor="hand2",command=detail)
  search_button.grid(row=2,column=0,columnspan=2)

def alertbox():
  messagebox.askyesno("confirmation","Do you want to save the data")
  mycursor.commit()

global vishal,pradeep,mycursor,mydb

vishal=Tk()
vishal.title("ARAVALIANS")
vishal.geometry("450x400")
vishal.minsize(450,400)
vishal.configure(bg="#1b03a3")
pradeep=Frame(vishal,bg="black",height=380,width=430))
pradeep.pack()
global Start_label=label(pradeep,text="welcome to Aravality",fg="white")
Start_label.place(relx=0.5,rely=1,anchor='center')
global connection_button=Button(pradeep,text='connect',activebackground="blue",activeforground="red",command=connect)
connection_button.place(relx=0.5,rely=1,anchor='center')
vishal.mainloop()
