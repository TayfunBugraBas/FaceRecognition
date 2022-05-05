from tkinter import *
from AppMain import AppMain



  
window = Tk()



window.title("deneme")    

  
  
def mainMenu():
      window.geometry("800x600")
      
      btn = Button(window,text="test", command = AppMain.faceRecognizerOpener)
      btn.pack()
      

mainMenu()
window.mainloop()
      