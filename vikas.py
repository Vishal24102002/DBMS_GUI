import pip
try:
  pip.main(["install"],["tk"])
  pip.main(["install"],["pyttsx3"])
  pip.main(["install"],["time"])
  import pyttsx3 as pt
  import time
  from coustomtkinter import *
except:
  import time
  import pyttsx3 as pt
  import customtkinter as ctk


Vikas=ctk.CTk()
Vikas.geometry("300x250")
Vikas.maxsize(500,250)
Vikas.minsize(500,250)
Vikas.title("Speech converter")
Vikas.configure(bg="green")

def speak(text,m,sp,v):
    try:
        engine=pt.init()
        Voices=engine.getProperty('voices')
        volu=engine.getProperty('volume')
        print(Voices)
        print(volu)
        engine.setProperty('voice',Voices[m].id) 
        engine.setProperty('rate',sp)
        engine.setProperty('volume',v)
        spend=engine.getProperty('rate')
        print("speed=",spend)
        engine.say(text)
        engine.runAndWait()
    except:
        print("error occured")

def volume(value):
    print(value)
    global v
    v=value
        
def speed(event):
    global s
    if voice_speed.get()=="VERY-FAST":
        s=350
    elif voice_speed.get()=="VERY-SLOW":
        s=50
    elif voice_speed.get()=="SLOW":
        s=150
    elif voice_speed.get()=="FAST":
        s=250
    else:
        s=200

def voice(event):
    global n
    if (voice_type.get()=="Voice 1"):
        n=0
    elif (voice_type.get()=="Voice 2"):
        n=1
    elif (voice_type.get()=="Voice 3"):
        n=2
    elif (voice_type.get()=="Voice 4"):
        n=3
    elif (voice_type.get()=="Voice 5"):
        n=4
def prin():
    global n,s,v
    print("n=",n)
    txt=text_area.get("1.0",'end-1c')
    print(txt)
    speak(txt,n,s,v)

Vikas1=ctk.CTkFrame(Vikas,fg_color="black",height=250,width=200)
Vikas1.pack(fill="both",expand=True)
Vikas2=ctk.CTkFrame(Vikas1,height=55,width=75)

n=ctk.IntVar()
s=ctk.IntVar()
v=ctk.IntVar()

empty_label=ctk.CTkLabel(Vikas1,text="",fg_color="black")
empty_label.grid(row=0,column=0)

voice_type=ctk.StringVar()
voice_type.set("choose voice")
voice_choice=ctk.CTkOptionMenu( Vikas1,values=[
"Voice 1",
"Voice 2",
"Voice 3",
"Voice 4",
"Voice 5"
],variable=voice_type,width=50,command=voice,dropdown_hover_color=("orange","yellow"))

voice_choice.grid(row=1,column=2)


voice_speed=ctk.StringVar()
voice_speed.set("Choose speed")
voice_cho=ctk.CTkOptionMenu( Vikas1,values=[
"VERY-FAST",
"FAST",
"NORMAL",
"SLOW",
"VERY-SLOW"
],variable=voice_speed,width=50,dropdown_hover_color=("orange","yellow"),command=speed)

voice_cho.grid(row=2,column=2)

vol_label=ctk.CTkLabel(Vikas1,text="volume",text_color="white")
vol_label.grid(row=3,column=2)
vol= ctk.CTkSlider(Vikas1, from_=0, to=1,number_of_steps=10,progress_color="yellow",width=150,command=volume)
vol.grid(row=3,column=3)

text_area = ctk.CTkTextbox(Vikas1,width=200,height=200,font=("Times New Roman", 15))
text_area.grid(padx=10,row=1,column=0,rowspan=4)

Vikas2.place(x=10,y=150)

Speak=ctk.CTkButton(Vikas1,text="CONVERT",hover_color="spring green",command=lambda:prin(),width=155,height=25)
Speak.grid(row=4,column=2,columnspan=2)

Vikas.mainloop()
