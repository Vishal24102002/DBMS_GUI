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
Vikas.title("Speach converter")

entry_label(Vikas,text=" ")
entry_label.grid(row=0,column=0)

entry1_label(Vikas,text=" ")
entry1_label.grid(row=0,column=4)


Text=Entry(Vikas,textvariable=Entry,font=('calibre',12,'normal'))
Text.grid(row=4,column=3,columnspan=4)

Speak=Button(vikas,text="convert",activebackground="blue",command=lambda:speak(Entry.get()))
Speak.grid(row=5,column=3,columnspan=4)

Vikas.mainloop
  
