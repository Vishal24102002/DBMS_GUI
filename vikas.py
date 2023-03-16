import pip
try:
  pip.main(["install"],["tk"])
  pip.main(["install"],["pyttsx3"])
  import pyttsx3
  from tkinter import *
except:
  import pyttsx3
  from tkinter import *

Vikas=tk()
Vikas.geometry("300x250")
Vikas.maxsize(300,250)
Vikas.minsize(300,250)
Vikas.title("Speech converter")
Vikas.configure(bg="green")

def speak():
   Engine=pt.init()
   Engine.say(Entry.get())
   Voices=engine.getProperty('voices') 
   print(Voices) 
   engine.setProperty('voice',Voices[1].id) 
   engine.runAndWait()

Vikas1=frame(Vikas,bg="black",highlightbackground="yellow",heightlightthickness=2)
Vikas1.pack()

Entry=StringVar()

Text=Entry(Vikas1,textvariable=Entry,font=('calibre',12,'normal'))
Text.place(x=,y=)

options=[
"Voice 1",
"Voice 2",
"Voice 3",
"Voice 4",
"Voice 5"
]
voice_type=StringVar()
voice_type.set("Voice 1")
voice_choice=OptionMenu(Vikas1, voice_type, *options)
voice_choice.pack()

Speak=Button(Vikas1,text="convert",activebackground="blue",command=speak)
Speak.place(x=,y=)
Vikas.mainloop()
  
