from tkinter import *
from AppMain import AppMain



  
window = Tk()



window.title("deneme")  
canvas = Canvas(window,height=450,width=750)  
frameA = Frame(window,bg='#add8e6')
frameB = Frame(window,bg='#add8e6')
frameC = Frame(window,bg='#add8e6')

  
  
def mainMenu():
      
      
      btn = Button(frameB,text="test", command = AppMain.faceRecognizerOpener)
      canvas.pack()
      btn.pack()
      frameA.place(relx=0.05,rely=0.01, relwidth=0.9,relheight=0.2)
      frameB.place(relx=0.05,rely=0.25, relwidth=0.3,relheight=0.7)
      frameC.place(relx=0.37,rely=0.25, relwidth=0.58,relheight=0.7)
     
      

mainMenu()
window.mainloop()
      