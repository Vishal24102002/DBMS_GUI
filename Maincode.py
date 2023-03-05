try:
  Import mysql-connector
  Import tkinter as tk
except:
  Import pip
  pip.main(['install','tk'])
  pip.main(['install','mysql-connector'])

def connect():
  mydb=mysql.connector.connect(host="localhost",user="root",password="vishal")
  mycursor=mydb.cursor()
  try:
    mycursor.execute("use aravalian")
  except:
    mycursor.execute("create database aravalian")
    mycursor.execute("use aravalian")
    print("connected successfully")
  connection_button.destroy()

vishal=Tk()
vishal.title("ARAVALIANS")
vishal.geometry("450x400")
vishal.minsize(450,400)
vishal.configure(bg="#1b03a3")
pradeep=Frame(vishal,bg="black",height=380,width=430))
pradeep.pack()
Start_label=label(pradeep,text="welcome to Aravality",fg="white")
Start_label.place(relx=0.5,rely=1,anchor='center')
connection_button=Button(pradeep,text='connect',activebackground="blue",activeforground="red",command=connect)
connection_button.place(relx=0.5,rely=1,anchor='center')
vishal.mainloop()
