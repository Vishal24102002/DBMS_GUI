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
global mycursor,vishal1,pradeep,clicked 
     
def speak(text):
    engine=pt.init()
    engine.say(text)
    Voices=engine.getProperty('voices') 
    print(Voices) 
    engine.setProperty('voice',Voices[1].id) 
    engine.runAndWait()
    
def update():
    
    mysql=" "
    mycusor.execute(mysql,)
    warning()

def connect(GET):
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
    NAME=staff_name.get()
    ID=staff_id.get()
    name_entry.delete(0,END)
    id_entry.delete(0,END)
    print("name =",NAME)
    print("id =",ID)
    mycursor.execute("show tables")
    print("get=",GET)
    if(GET=="faculities"):
        n=('aravality',)
    elif(GET=="students"):
        n=('student',)
    else:
        #n=('aravality',)
        speak("select the required column")
    vishal1.minsize(400,420)
    print("n",n)
    detail_frame=Frame(pradeep,highlightbackground="red",highlightthickness=3)
    detail_frame.place(x=25,y=150,height=250,width=350)
    
    detail1=Label(detail_frame,text="ID",font=('calibre',10,'normal'),fg="black",borderwidth=2,relief="solid")
    detail2=Label(detail_frame,text="NAME",font=('calibre',10,'normal'),fg="black",borderwidth=2,relief="solid")
    detail3=Label(detail_frame,text="SALARY",font=('calibre',10,'normal'),fg="black",borderwidth=2,relief="solid")
    detail4=Label(detail_frame,text="DATE OF JOINING",font=('calibre',10,'normal'),fg="black",borderwidth=2,relief="solid")
    detail5=Label(detail_frame,text="DATE OF BIRTH",font=('calibre',10,'normal'),fg="black",borderwidth=2,relief="solid")
    result1=Label(detail_frame,text="",font=('calibre',10,'normal'),fg="black")
    result2=Label(detail_frame,text="",font=('calibre',10,'normal'),fg="black")
    result3=Label(detail_frame,text="",font=('calibre',10,'normal'),fg="black")
    result4=Label(detail_frame,text="",font=('calibre',10,'normal'),fg="black")
    result5=Label(detail_frame,text="",font=('calibre',10,'normal'),fg="black")
    
    detail1.place(x=0,y=0)
    detail2.place(x=0,y=30)
    detail3.place(x=0,y=60)
    detail4.place(x=0,y=90)
    detail5.place(x=0,y=120)
    result1.place(x=200,y=0)
    result2.place(x=200,y=30)
    result3.place(x=200,y=60)
    result4.place(x=200,y=90)
    result5.place(x=200,y=120)
    for tables in mycursor:
        print(tables)
        if tables!=n:
            speak("not found, creating one ")
            mycursor.reset()
            mycursor.execute(cmd="create table %s (name varchar(12),salary int(4),date_joining int,date_of_birth int(6))",n)
        elif tables==n:
            try:
                mycursor.execute("select * from aravality where name= %s",NAME)
                faculities_details=mycursor.fetchall()
                print("total rows in details",mycursor.rowcount)
                for row in faculities_details:
                    result1.set(text=row[0])
                    result2.set(text=row[1])
                    result3.set(text=row[2])
                    result4.set(text=row[3])
                    result5.set(text=row[4])
                cursor.reset()
                    
            except:
                speak("no such data found")
                for widgets in frame.winfo_children():
                    widgets.destroy()
                    error_label=Label(detail_frame,text=" ",fg="red",font=('calibre',12,'normal'))
                    error_label.grid(row=0,column=0,columnspan=3,rowspan=3)
                    error_label.config(text="ERROR")
                    break
        break()
                
    update_button=Button(pradeep,text="update",activebackground="green",activeforground="blue",font=('calibre',10,'normal'),command=update)  
    update_button.pack(side=Bottom,padx=120)


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
clicked.set("faculities")
drop = OptionMenu( start_frame, clicked, *options )
name_label=Label(start_frame,text="Staff-Name",bg="yellow",fg="black",font=('calibre',12,'normal'))
name_entry=Entry(start_frame,textvariable=staff_name,font=('calibre',13,'normal'))
id_label=Label(start_frame,text="Staff-ID",fg="black",bg="yellow",font=('calibre',12,'normal'))
id_entry=Entry(start_frame,textvariable=staff_id,font=('calibre',13,'normal'))



#widgets packing
empty_label.grid(row=0,column=1)
drop.grid(row=2,columnspan=3,sticky=N)
id_entry.grid(padx=5,row=4,column=1)
id_label.grid(padx=5,row=4,column=0)
name_entry.grid(padx=5,row=3,column=1)
name_label.grid(padx=5,row=3,column=0)

search_button=Button(start_frame,text="search",cursor="hand2",activebackground="blue",relief="sunken",command=lambda:connect(clicked.get()),width=20)
search_button.grid(row=5,columnspan=3)

vishal1.mainloop()  
