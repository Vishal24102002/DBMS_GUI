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
global mycursor,vishal1,pradeep,clicked,start_frame
     
def speak(text):
    engine=pt.init()
    engine.say(text)
    Voices=engine.getProperty('voices') 
    print(Voices) 
    engine.setProperty('voice',Voices[1].id) 
    engine.runAndWait()
    
    
def update():
    update_tk=Toplevel()
    update_tk.configure(bg="blue")
    
    update=Frame(update_tk,bg="black")
    update.pack(padx=20,pady=20,expand=True,fill="both")
    
    
    mycusor.execute("update "+m+" set "+column+"="+value+"where name="'''"'''+updated_name+'''"''')
    warning()

def connect(GET):
    mydb=mysql.connector.connect(user="root",password="vishal",host="localhost",consume_results=True)
    mycursor=mydb.cursor()
    try:
        mycursor.execute("use aravali")
        print("found it ")
    except:
        mycursor.execute("create database aravali")
        mycursor.execute("use aravali")
        print("not found so created")
    speak("connected successfully")
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
        m="aravality"
    elif(GET=="students"):
        n=('student',)
        m="student"
    else:
        speak("select the required column")
    vishal1.minsize(400,500)
    print("n",n)
    detail_frame=Frame(start_frame,highlightbackground="red",highlightthickness=3)
    detail_frame.place(x=0,y=150,height=250,width=350)
    
    data1=StringVar()
    data2=StringVar()
    data3=StringVar()
    data4=StringVar()
    data5=StringVar()
    
    
    detail1=Label(detail_frame,text="ID",font=('calibre',10,'normal'),fg="black",borderwidth=2,relief="solid")
    detail2=Label(detail_frame,text="NAME",font=('calibre',10,'normal'),fg="black",borderwidth=2,relief="solid")
    detail3=Label(detail_frame,text="SALARY",font=('calibre',10,'normal'),fg="black",borderwidth=2,relief="solid")
    detail4=Label(detail_frame,text="DATE OF JOINING",font=('calibre',10,'normal'),fg="black",borderwidth=2,relief="solid")
    detail5=Label(detail_frame,text="DATE OF BIRTH",font=('calibre',10,'normal'),fg="black",borderwidth=2,relief="solid")
    result1=Label(detail_frame,text="",textvariable=data1,font=('calibre',10,'normal'),fg="black",relief="solid")
    result2=Label(detail_frame,text="",textvariable=data2,font=('calibre',10,'normal'),fg="black",relief="solid")
    result3=Label(detail_frame,text="",textvariable=data3,font=('calibre',10,'normal'),fg="black",relief="solid")
    result4=Label(detail_frame,text="",textvariable=data4,font=('calibre',10,'normal'),fg="black",relief="solid")
    result5=Label(detail_frame,text="",textvariable=data5,font=('calibre',10,'normal'),fg="black",relief="solid")
    
    update_button=Button( start_frame,text="update",activebackground="red",font=('calibre',10,'normal'),command=update,relief="solid")  
    update_button.place(x=0,y=400,width=175,height=35)
    insert_button=Button( start_frame,text="insert",activebackground="red",font=('calibre',10,'normal'),command=update,relief="solid")  
    insert_button.place(x=175,y=400,width=175,height=35)
    close_button=Button( start_frame,text="close",activebackground="red",font=('calibre',10,'normal'),command=Close,relief="solid")  
    close_button.place(x=0,y=435,width=350,height=40)
    
    detail1.place(x=0,y=0,width=200)
    detail2.place(x=0,y=20,width=200)
    detail3.place(x=0,y=40,width=200)
    detail4.place(x=0,y=60,width=200)
    detail5.place(x=0,y=80,width=200)
    result1.place(x=175,y=0,width=170)
    result2.place(x=175,y=20,width=170)
    result3.place(x=175,y=40,width=170)
    result4.place(x=175,y=60,width=170)
    result5.place(x=175,y=80,width=170)
    
    for tables in mycursor:
        print(tables)
        if tables!=n:
            speak("not found, creating one ")
            mycursor.reset()
            mycursor.execute("create table "+m+"(name varchar(12),salary int(4),joining int(9),birthday int(6))")
            mycursor.reset()
        elif tables==n:
            try:
                if (len(NAME)==0):
                    speak("enter the columns")
                    for widgets in Frame.winfo_children(detail_frame):
                        widgets.destroy()
                    error_label1=Label(detail_frame,text=" ",fg="purple",font=('calibre',18,'normal'))
                    error_label1.place(x=90,y=90)
                    error_label1.config(text="record not found")
                    
                else:
                    mycursor.execute("select * from "+m+" where name="+'''"'''+NAME+'''"''')
                    faculities_details=mycursor.fetchall()
                    speak("data found")
                    print("total rows in details",mycursor.rowcount)
                    for row in faculities_details:
                        data1.set(row[0])
                        data2.set(row[1])
                        data3.set(row[2])
                        data4.set(row[3])
            except:
                speak("no such data found")
                for widgets in Frame.winfo_children(detail_frame):
                    widgets.destroy()
                
                
                error_label=Label(detail_frame,text=" ",fg="red",font=('calibre',18,'normal'))
                error_label.place(x=130,y=90)
                error_label.config(text="ERROR")
                
        break
                
def Close():
    vishal1.destroy()

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
name_label=Label(start_frame,text=" *Staff-Name",bg="yellow",fg="black",font=('calibre',12,'normal'))
name_entry=Entry(start_frame,textvariable=staff_name,font=('calibre',13,'normal'))
id_label=Label(start_frame,text=" *Staff-ID",fg="black",bg="yellow",font=('calibre',12,'normal'))
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
