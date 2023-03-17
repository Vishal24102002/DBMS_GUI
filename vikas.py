import pip
try:
  pip.main(["install"],["tk"])
  pip.main(["install"],["pyttsx3"])
  pip.main(["install"],["time"])
  import pyttsx3 as pt
  import time
  from tkinter import *
except:
  import time
  import pyttsx3 as pt
  from tkinter import *

Vikas=tk()
Vikas.geometry("300x250")
Vikas.maxsize(300,250)
Vikas.minsize(300,250)
Vikas.title("Speech converter")
Vikas.configure(bg="green")

def speak():
   time.sleep(1000)
   if (voice_type="Voice 1"):
     n=0
   elif (voice_type="Voice 2"):
     n=1
   elif (voice_type="Voice 3"):
     n=2
   elif (voice_type="Voice 4"):
     n=3
   if (voice_type="Voice 5"):
     n=4
   else:
     n=0
   engine=pt.init()
   engine.say(Entry.get())
   Voices=engine.getProperty('voices') 
   print(Voices) 
   engine.setProperty('voice',Voices[n].id) 
   engine.runAndWait()

Vikas1=Frame(Vikas,bg="black",highlightbackground="yellow",heightlightthickness=2)
Vikas1.pack()
Vikas2=Frame(Vikas)

Entry=StringVar()
options=[
"Voice 1",
"Voice 2",
"Voice 3",
"Voice 4",
"Voice 5"
]
voice_type=StringVar()
voice_type.set("Voice 1")
voice_choice=OptionMenu( Vikas1,voice_type ,*options)
voice_choice.pack()
Text=Entry(Vikas1,textvariable=Entry,font=('calibre',12,'normal'))
Text.place(x=10,y=100,height=50,width=75) 

Vikas2.place(x=10,y=150,height=55,width=75)

Speak=Button(Vikas1,text="convert",activebackground="blue",command=speak)
Speak.place(x=25,y=205,width=15)

Vikas.mainloop()
  
