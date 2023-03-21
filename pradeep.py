import time

import pip

try:
    from tkinter import *
    import pyttsx3 as pt
    from tkinter import messagebox
    import mysql.connector
    import customtkinter as ctk
except:
    pip.main(["install"], ["tk"])
    pip.main(["install"], ["pyttsx3"])
    pip.main(["install"], ["mysql-connector"])
    pip.main(["install"], ["customtkinter"])
    from tkinter import *
    import customtkinter as ctk
    import pyttsx3 as pt
    from tkinter import messagebox
    import mysql.connector

count = 0


def th():
    global count
    count += 1
    if (count % 2 == 0):
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")


def speak(text):
    engine = pt.init()
    engine.say(text)
    Voices = engine.getProperty('voices')
    print(Voices)
    engine.setProperty('voice', Voices[1].id)
    engine.runAndWait()


def chossen():
    if (cho == "name"):
        name_label = ctk.CTkLabel(update, text="name", font=('calibre', 12, 'normal'), text_color="white",
                                  fg_color="black", width=200, height=20)
    elif (cho == "Id"):
        name_label = ctk.CTkLabel(update, text="ID", font=('calibre', 12, 'normal'), text_color="white",
                                  fg_color="black", width=200, height=20)
    elif (cho == "experience"):
        name_label = ctk.CTkLabel(update, text="experience", font=('calibre', 12, 'normal'), text_color="white",
                                  fg_color="black", width=200, height=20)
    else:
        name_label = ctk.CTkLabel(update, text="chose", font=('calibre', 12, 'normal'), text_color="white",
                                  fg_color="black", width=200, height=20)
    from_name = ctk.CTkEntry(update, placeholder_text=upname, font=('calibre', 12, 'normal'), width=200, height=25)
    # update_id=ctk.CTkEntry(update,placeholder_text=upid,font=('calibre',12,'normal'),width=200,height=25)

    print(choice.get())

    # update_id.place(x=0,y=)
    from_label.place(x=0, y=35)
    name_label.place(x=35, y=105)
    from_name.place(x=235, y=105)


def update():
    start_frame.forget()

    start_frame2 = ctk.CTkFrame(master=pradeep, fg_color=("black", "red"))
    start_frame2.pack(pady=5, padx=10, expand=True, fill="both")

    update_tk = ctk.CTkFrame(start_frame2, fg_color=("black", "yellow"))
    update_tk.pack(padx=0, pady=0, fill="both", expand=True)
    vishal1.minsize(500, 455)

    update = ctk.CTkFrame(update_tk, fg_color="black")
    update.pack(padx=10, pady=10, expand=True, fill="both")

    heading_label = ctk.CTkLabel(update, text="DETAILS", fg_color="red", font=('calibre', 20, 'normal'), width=485)
    heading_label.place(x=0, y=0)

    upname = StringVar()
    chose = ctk.StringVar()
    chose.set("choose one")

    from_label = ctk.CTkLabel(update, text="from column", fg_color="blue", text_color="red",
                              font=('calibre', 15, 'normal'), width=480, height=25)
    choice = ctk.CTkOptionMenu(update, values=["name", "Id", "experience"], variable=chose,
                               dropdown_hover_color=("orange", "yellow"), button_color="spring green")
    choice.place(x=0, y=70)

    save_button = ctk.CTkButton(update, text="save", text_color="yellow", hover_color="lime", cursor="hand2", width=230,
                                height=30)
    save_button.place(x=0, y=370)
    cancel_button = ctk.CTkButton(update, text="cancel", text_color="yellow", cursor="hand2", hover_color="lime",
                                  command=lambda: cancel(start_frame2), width=230, height=30)
    cancel_button.place(x=250, y=370)
    ccccccccccccccccc


def insert():
    start_frame.forget()
    vishal1.minsize(400, 415)
    vishal1.maxsize(400, 415)

    start_frame1 = ctk.CTkFrame(master=pradeep, fg_color=("black", "red"))
    start_frame1.pack(pady=5, padx=10, expand=True, fill="both")
    insert_tk = ctk.CTkFrame(start_frame1, fg_color=("black", "yellow"))
    insert_tk.pack(pady=0, padx=0, expand=True, fill='both')

    head_label = ctk.CTkLabel(insert_tk, text="details", fg_color="red", font=('calibre', 18, 'normal'), width=380,
                              height=25)
    head_label.pack(padx=10, pady=5)

    insert = ctk.CTkFrame(insert_tk, fg_color=("black", "navy"))
    insert.pack(padx=10, pady=5, expand=True, fill="both")

    inserted_name = StringVar()
    inserted_age = StringVar()
    inserted_phone = StringVar()
    inserted_jyear = StringVar()
    inserted_exp = StringVar()

    insert_emplabel = ctk.CTkLabel(insert, text=" ", fg_color=("black", "navy"))
    insert_emplabel.grid(row=0, column=0)

    insert_namelabel = ctk.CTkLabel(insert, text="updated-name", text_color=("red", "white"),
                                    fg_color=("black", "navy"))
    insert_namelabel.grid(row=1, column=0)
    insert_name = ctk.CTkEntry(insert, placeholder_text=inserted_name)
    insert_name.grid(row=1, column=1)
    insert_agelabel = ctk.CTkLabel(insert, text="updated-age", text_color=("red", "white"), fg_color=("black", "navy"))
    insert_agelabel.grid(row=2, column=0)
    insert_age = ctk.CTkEntry(insert, placeholder_text=inserted_age)
    insert_age.grid(row=2, column=1)
    insert_phonelabel = ctk.CTkLabel(insert, text="updated-phone-number", text_color=("red", "white"),
                                     fg_color=("black", "navy"))
    insert_phonelabel.grid(row=3, column=0)
    insert_phone = ctk.CTkEntry(insert, placeholder_text=inserted_phone)
    insert_phone.grid(row=3, column=1)
    insert_jyearlabel = ctk.CTkLabel(insert, text="updated-year of joining", text_color=("red", "white"),
                                     fg_color=("black", "navy"))
    insert_jyearlabel.grid(row=4, column=0)
    insert_jyear = ctk.CTkEntry(insert, placeholder_text=inserted_jyear)
    insert_jyear.grid(row=4, column=1)
    insert_explabel = ctk.CTkLabel(insert, text="updated-experience", text_color=("red", "white"),
                                   fg_color=("black", "navy"))
    insert_explabel.grid(row=5, column=0)
    insert_exp = ctk.CTkEntry(insert, placeholder_text=inserted_exp)
    insert_exp.grid(row=5, column=1)

    save_button = ctk.CTkButton(insert, text="save", fg_color="red", hover_color="lime", cursor="hand2", width=190,
                                height=25)
    save_button.place(x=0, y=270)
    cancel_button = ctk.CTkButton(insert, text="cancel", fg_color="red", hover_color="lime", cursor="hand2",
                                  command=lambda: cancel(start_frame1), width=190, height=25)
    cancel_button.place(x=190, y=270)


def cancel(c):
    toplevel = Toplevel(vishal1)
    toplevel.title("warning")
    x_position = 300
    y_position = 200
    toplevel.geometry(f"300x100+{x_position}+{y_position}")

    l1 = Label(toplevel, image="::tk::icons::question")
    l1.grid(row=0, column=0, pady=(7, 0), padx=(10, 30), sticky="e")
    l2 = Label(toplevel, text="Are you sure you want to Quit")
    l2.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")

    b1 = Button(toplevel, text="Yes", command=lambda: reset(toplevel, c), width=10)
    b1.grid(row=1, column=1, padx=(2, 35), sticky="e")
    b2 = Button(toplevel, text="No", command=lambda: destroy(toplevel), width=10)
    b2.grid(row=1, column=2, padx=(2, 35), sticky="e")


def reset(db, c):
    vishal1.minsize(360, 500)
    vishal1.maxsize(360, 500)
    c.destroy()
    start_frame.pack(pady=5, padx=10, expand=True, fill="both")
    db.destroy()


def destroy(db):
    db.destroy()


def connect(GET):
    mydb = mysql.connector.connect(user="root", password="vishal", host="localhost", consume_results=True)
    mycursor = mydb.cursor()
    try:
        mycursor.execute("use aravali")
        print("found it ")
    except:
        mycursor.execute("create database aravali")
        mycursor.execute("use aravali")
        print("not found so created")
    speak("connected successfully")
    NAME = name_entry.get()
    ID = id_entry.get()
    name_entry.delete(0, END)
    id_entry.delete(0, END)
    print("name =", NAME)
    print("id =", ID)
    mycursor.execute("show tables")
    print("get=", GET)
    if (GET == "faculities"):
        n = ('aravality',)
        m = "aravality"
    elif (GET == "students"):
        n = ('student',)
        m = "student"
    else:
        speak("select the required column")
        return
    vishal1.minsize(360, 500)
    vishal1.maxsize(360, 500)
    print("n", n)
    detail_frame = ctk.CTkFrame(start_frame, fg_color=("black", "black"), height=250, width=350)
    detail_frame.place(x=0, y=155)

    data1 = StringVar()
    data2 = StringVar()
    data3 = StringVar()
    data4 = StringVar()
    data5 = StringVar()
    data6 = StringVar()
    data7 = StringVar()
    data8 = StringVar()
    if (m=="aravality"):
        detail1 = ctk.CTkLabel(detail_frame, text="ID", font=('calibre', 14, 'normal'), text_color=("red", "yellow"),
                               width=200)
        detail2 = ctk.CTkLabel(detail_frame, text="NAME", font=('calibre', 14, 'normal'), text_color=("red", "yellow"),
                               width=200)
        detail3 = ctk.CTkLabel(detail_frame, text="SALARY", font=('calibre', 14, 'normal'),
                               text_color=("red", "yellow"),
                               width=200)
        detail4 = ctk.CTkLabel(detail_frame, text="YEAR OF JOINING", font=('calibre', 14, 'normal'),
                               text_color=("red", "yellow"), width=200)
        detail5 = ctk.CTkLabel(detail_frame, text="YEAR OF BIRTH", font=('calibre', 14, 'normal'),
                               text_color=("red", "yellow"), width=200)
        detail6 = ctk.CTkLabel(detail_frame, text="DATE OF BIRTH", font=('calibre', 14, 'normal'),
                               text_color=("red", "yellow"), width=200)
        detail7 = ctk.CTkLabel(detail_frame, text="MOBILE NUMBER", font=('calibre', 14, 'normal'),
                               text_color=("red", "yellow"), width=200)
        detail8 = ctk.CTkLabel(detail_frame, text="YEARS OF EXPERIENCE", font=('calibre', 14, 'normal'),
                               text_color=("red", "yellow"), width=200)
    # detail5=ctk.CTkLabel(detail_frame,text="DATE OF BIRTH",font=('calibre',10,'normal'),text_color=("red","yellow"),width=200)
    # detail5=ctk.CTkLabel(detail_frame,text="DATE OF BIRTH",font=('calibre',10,'normal'),text_color=("red","yellow"),width=200)
    # detail5=ctk.CTkLabel(detail_frame,text="DATE OF BIRTH",font=('calibre',10,'normal'),text_color=("red","yellow"),width=200)
    # detail5=ctk.CTkLabel(detail_frame,text="DATE OF BIRTH",font=('calibre',10,'normal'),text_color=("red","yellow"),width=200)
    else:
        detail1 = ctk.CTkLabel(detail_frame, text="ID", font=('calibre', 14, 'normal'), text_color=("red", "yellow"), width=200)
        detail2 = ctk.CTkLabel(detail_frame, text="NAME", font=('calibre', 14, 'normal'), text_color=("red", "yellow"),width=200)
        detail3 = ctk.CTkLabel(detail_frame, text="Branch", font=('calibre', 14, 'normal'),text_color=("red", "yellow"),width=200)
        detail4 = ctk.CTkLabel(detail_frame, text="Section", font=('calibre', 14, 'normal'),text_color=("red", "yellow"), width=200)
        detail5 = ctk.CTkLabel(detail_frame, text="Date of Birth", font=('calibre', 14, 'normal'),text_color=("red", "yellow"), width=200)
        detail6 = ctk.CTkLabel(detail_frame, text="Email", font=('calibre', 14, 'normal'),text_color=("red", "yellow"), width=200)
        detail7 = ctk.CTkLabel(detail_frame, text="MOBILE NUMBER", font=('calibre', 14, 'normal'),text_color=("red", "yellow"), width=200)
        # detail8 = ctk.CTkLabel(detail_frame, text="YEARS OF EXPERIENCE", font=('calibre', 14, 'normal'),text_color=("red", "yellow"), width=200)
    result1 = ctk.CTkLabel(detail_frame, text="", textvariable=data1, font=('calibre', 14, 'normal'), text_color=("white", "white"), width=170)
    result2 = ctk.CTkLabel(detail_frame, text="", textvariable=data2, font=('calibre', 14, 'normal'),text_color=("white", "white"), width=170)
    result3 = ctk.CTkLabel(detail_frame, text="", textvariable=data3, font=('calibre', 14, 'normal'), text_color=("white", "white"), width=170)
    result4 = ctk.CTkLabel(detail_frame, text="", textvariable=data4, font=('calibre', 14, 'normal'),text_color=("white", "white"), width=170)
    result5 = ctk.CTkLabel(detail_frame, text="", textvariable=data5, font=('calibre', 14, 'normal'), text_color=("white", "white"), width=170)
    result6 = ctk.CTkLabel(detail_frame, text="", textvariable=data6, font=('calibre', 14, 'normal'),text_color=("white", "white"), width=170)
    result7 = ctk.CTkLabel(detail_frame, text="", textvariable=data7, font=('calibre', 14, 'normal'),text_color=("white", "white"), width=170)
    result8 = ctk.CTkLabel(detail_frame, text="", textvariable=data8, font=('calibre', 14, 'normal'),text_color=("white", "white"), width=170)

    update_button = ctk.CTkButton(start_frame, text="update", font=('calibre', 14, 'normal'),hover_color=("lime", "aqua"), width=175, height=35, command=update)
    update_button.place(x=0, y=400)
    insert_button = ctk.CTkButton(start_frame, text="insert", hover_color=("lime", "aqua"),font=('calibre', 14, 'normal'), width=175, height=35, command=insert)
    insert_button.place(x=175, y=400)
    close_button = ctk.CTkButton(start_frame, text="close", hover_color=("red", "hot pink"), font=('calibre', 14, 'normal'), command=Close, width=350, height=40)
    close_button.place(x=0, y=435)

    detail1.place(x=0, y=0)
    detail2.place(x=0, y=20)
    detail3.place(x=0, y=40)
    detail4.place(x=0, y=60)
    detail5.place(x=0, y=80)
    detail6.place(x=0, y=100)
    detail7.place(x=0, y=120)
    if(m=="aravality"):
        detail8.place(x=0, y=140)

    result1.place(x=175, y=0)
    result2.place(x=175, y=20)
    result3.place(x=175, y=40)
    result4.place(x=175, y=60)
    result5.place(x=175, y=80)
    result6.place(x=175, y=100)
    result7.place(x=175, y=120)
    result8.place(x=175, y=140)

    jyear_label.destroy()
    jyear_entry.destroy()

    for tables in mycursor:
        print(tables)
        # if (tables != n):
        #     try:
        #         speak("not found, creating one ")
        #         mycursor.reset()
        #         mycursor.execute("create table " + m + "(name varchar(12),salary int(4),joining int(9),birthday int(6))")
        #         mycursor.reset()
        #     except:
        #         print("hello")
        kyuki=0
        if tables == n:
            try:
                if (len(NAME) == 0 and kyuki!=0 ):
                    speak("enter the columns")
                    for widgets in Frame.winfo_children(detail_frame):
                        widgets.destroy()
                    error_label1 = ctk.CTkLabel(detail_frame, text="RECORD NOT FOUND", text_color=("red", "red"),
                                                font=('calibre', 18, 'normal'))
                    error_label1.place(x=90, y=90)
                    speak("record not found")


                else:
                    try:
                        if((len(NAME) != 0) and (len(ID)==0)):
                            mycursor.execute("select * from " + m + " where FirstName=" + '''"''' + NAME + '''"''')
                        elif((len(ID)!=0) and (len(NAME)==0)):
                            mycursor.execute("select * from " + m + " where StudentID=" + '''"''' + ID + '''"''')
                        elif((len(ID)!=0) and (len(NAME)!=0)):
                            mycursor.execute("select * from " + m + " where StudentID=" + '''"''' + ID + '''"'''+"&& firstname="+'''"''' + NAME + '''"''')
                        else:
                            prin("name")
                    except:
                        mycursor.execute("select * from " + m + " where Name=" + '''"''' + NAME + '''"''')
                faculities_details = mycursor.fetchall()
                speak("data found")
                print("total rows in details", mycursor.rowcount)
                if(mycursor.rowcount!=0):
                    kyuki=kyuki+1
                    if(m=="student"):
                        for row in faculities_details:
                          data1.set(row[4])
                          data2.set(row[0] + row[1])
                          data3.set(row[7])
                          data4.set(row[3])
                          data5.set(row[5])
                          data6.set(row[2])
                          data7.set(row[6])
                    else:
                        for row in faculities_details:
                         # data1.set(row[4])
                         data2.set(row[0])
                         data3.set(row[1])
                         data4.set(row[2])
                         data5.set(row[3])

                else:
                    speak("no such data found")
                    for widgets in Frame.winfo_children(detail_frame):
                        widgets.destroy()

                    error_label = ctk.CTkLabel(detail_frame, text="DATA NOT FOUND", fg_color=("black", "black"),
                                               text_color=("red", "white"), font=('calibre', 18, 'normal'))
                    error_label.place(x=100, y=90)


            except:
                speak("no such data found")
                for widgets in Frame.winfo_children(detail_frame):
                    widgets.destroy()

                error_label = ctk.CTkLabel(detail_frame, text="ERROR", fg_color=("black", "black"),
                                           text_color=("red", "white"), font=('calibre', 18, 'normal'))
                error_label.place(x=130, y=90)


def Close():
    vishal1.destroy()


vishal1 = ctk.CTk()
vishal1.title("Aravality")
vishal1.geometry("330x250")
vishal1.minsize(330, 250)
vishal1.maxsize(330, 200)
ctk.set_appearance_mode("light")
# vishal1.iconbitmap(r'C:\Users\Admin\Documents\vishalproject\logo.ico')
vishal1.configure(fg_color=("black", "blue"))

staff_id = ctk.StringVar()
staff_name = ctk.StringVar()
staff_jyear = ctk.StringVar()


pradeep = ctk.CTkFrame(vishal1, fg_color=("yellow", "blue"))
pradeep.pack(fill="both", expand=True)

start_frame = ctk.CTkFrame(master=pradeep, fg_color=("black", "red"))
start_frame.pack(pady=5, padx=10, expand=True, fill="both")

# label creation
empty_label = ctk.CTkLabel(start_frame, text="", fg_color=("black", "red"))
# datatype of menu text
clicked = ctk.StringVar()
clicked.set("select any one")
drop = ctk.CTkOptionMenu(start_frame, values=["faculities", "students"], variable=clicked, dropdown_hover_color=("orange", "yellow"), button_color="spring green")


name_label = ctk.CTkLabel(start_frame, text=" *Staff-Name", fg_color=("black", "red"), text_color=("white", "black"),font=('calibre', 12, 'normal'))
name_entry = ctk.CTkEntry(start_frame, placeholder_text=staff_name, font=('calibre', 13, 'normal'))
id_label = ctk.CTkLabel(start_frame, text=" *Staff-ID", text_color=("white", "black"), fg_color=("black", "red"),font=('calibre', 12, 'normal'))
id_entry = ctk.CTkEntry(start_frame, placeholder_text=staff_id, font=('calibre', 13, 'normal'))
jyear_label = ctk.CTkLabel(start_frame, text=" year of joining", fg_color=("black", "red"),text_color=("white", "black"), font=('calibre', 12, 'normal'))
jyear_entry = ctk.CTkEntry(start_frame, placeholder_text=staff_jyear, font=('calibre', 13, 'normal'))
jyear_entry.grid(padx=5, pady=5, row=5, column=1)
jyear_label.grid(padx=5, row=5, column=0)

# widgets packing
empty_label.grid(row=0, column=1)
drop.grid(row=2, columnspan=3, sticky="n")
id_entry.grid(padx=5, pady=5, row=4, column=1)
id_label.grid(padx=5, pady=5, row=4, column=0)
name_entry.grid(padx=5, pady=5, row=3, column=1)
name_label.grid(padx=5, pady=5, row=3, column=0)

theme_button = ctk.CTkButton(start_frame, text="theme", hover_color=("salmon", "navy"), cursor="hand2", command=th,
                             width=20)
theme_button.grid(row=0, column=3)

search_button = ctk.CTkButton(start_frame, text="search", cursor="hand2", hover_color=("seagreen", "emerald"),
                              command=lambda: connect(clicked.get()), height=20, width=100)
search_button.grid(row=6, columnspan=3)

vishal1.mainloop()
