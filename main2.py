import pip
try:
    from tkinter import *
    import pyttsx3 as pt
    from tkinter import messagebox
    import mysql.connector
    print("true")
    
except:
    pip.main(["install"],["tk"])
    pip.main(["install"],["pyttsx3"])
    pip.main(["install"],["mysql-connector"])
    from tkinter import *
    import pyttsx3 as pt
    from tkinter import messagebox
    import mysql.connector
global mycursor,vishal1,pradeep  
     
def speak(text):
    engine=pt.init()
    engine.say(text)
    Voices=engine.getProperty('voices') 
    print(Voices) 
    engine.setProperty('voice',Voices[1].id) 
    engine.runAndWait()

def search(mycursor):
    NAME=staff_name.get()
    ID=staff_id.get()
    print("name =",NAME)
    print("id =",ID)
    mycursor.execute("show tables")
    n=('aravality',)
    for tables in mycursor:
        print(tables)
        if tables!=n:
            speak("not found, creating one ")
            mycursor.execute("create table aravality(name varchar(12),salary int(4),date_joining int,date_of_birth int(6))")
        if tables==n:
            try:
                mycursor.execute("select * from aravality where name="+NAME+"& age="+ID)
                faculities_details=mycursor.fetchall()
                print("total rows in details",mycursor.rowcount)
            except:
                speak("no such data found")
                break
    vishal1.minsize(350,420)
    detail_frame=Frame(pradeep)
    detail_frame.place(x=25,y=100,height=300,width=300)
    
def connect():
    mydb=mysql.connector.connect(user="root",password="vishal",host="localhost")
    mycursor=mydb.cursor()
    try:
        mycursor.execute("use aravali")
        print("found it ")
    except:
        mycursor.execute("create database aravali")
        mycursor.execute("use aravali")
        print("not found so created")
    speak("connected successfully")
    warning(mydb)
    search(mycursor)

def warning(mydb):
    messagebox.askyesno("show warning","do you want to continue?")
    mydb.commit()

vishal1=Tk()
vishal1.title("Aravality")
vishal1.geometry("350x350")
vishal1.minsize(350,350)
vishal1.iconbitmap(r'C:\Users\Admin\Documents\vishalproject\logo.ico')
vishal1.configure(bg="black")
staff_id=StringVar()
staff_name= StringVar()
pradeep=Frame(vishal1,bg="black")
pradeep.pack(fill="both",expand=True)

start_frame=Frame(pradeep,bg="yellow")
start_frame.pack(pady=15,padx=25,expand=True,fill='both')

# label creation 
empty_label=Label(start_frame,text="",bg="yellow")

options = [
"faculities",
"students"
] 
# datatype of menu text
clicked = StringVar() 
clicked.set( "select the below" )
drop = OptionMenu( start_frame, clicked , *options )
name_label=Label(start_frame,text="Staff-Name",bg="yellow",fg="black",font=('calibre',12,'normal'))
name_entry=Entry(start_frame,textvariable=staff_name,font=('calibre',13,'normal'))
id_label=Label(start_frame,text="Staff-ID",fg="black",bg="yellow",font=('calibre',12,'normal'))
id_entry=Entry(start_frame,show="@",textvariable=staff_id,font=('calibre',13,'normal'))

#widgets packing
empty_label.grid(row=0,column=1)
drop.grid(row=2,columnspan=3,sticky=N)
id_entry.grid(padx=5,row=4,column=1)
id_label.grid(padx=5,row=4,column=0)
name_entry.grid(padx=5,row=3,column=1)
name_label.grid(padx=5,row=3,column=0)

search_button=Button(start_frame,text="search",cursor="hand2",activebackground="blue",relief="sunken",command=connect)
search_button.grid(row=5,columnspan=2)
vishal1.mainloop()  
