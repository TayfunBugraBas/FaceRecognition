from tkinter import *
from AppMain import AppMain
from tkinter import ttk
  







##################MAİN###################
window = Tk()

window.protocol("WM_DELETE_WINDOW",AppMain.Disable)


window.title("FaceRecognition")  

def ExitProg():
    AppMain.destroyer()
    window.destroy()

def inputHandler():
    inputValue=textBox.get("1.0","end-1c")
    AppMain.inputTaker(inputValue) 
    
    


canvas = Canvas(window,height=350,width=600)   
frameA = Frame(window,bg='#add8e6')
frameB = Frame(window,bg='#add8e6')
frameC = Frame(window,bg='#add8e6')

btnC = Button(frameA ,text="Çıkış", command = ExitProg  ,width=10,height=1,font=("Verdana 10 bold",10))
btnC.pack()

    
inputValue='NOT-IDENTIFIED'   
 
Label( frameC, text="isim Giriniz ",bg='#add8e6', font=("Verdana 10 bold",20),width=40,height=1).pack(padx=10,pady=10) 
 
textBox=Text(frameC, height=2, width=100)
textBox.pack()
 
      
btn = Button(frameB,text="Beni Tanı!", command = AppMain.faceRecognizerOpener,width=20,height=20,font=("Verdana 10 bold",20))
Label(frameA, text="Yüz Tanıma Sistemi",bg='#add8e6', font=("Verdana 10 bold",20),width=20,height=20).pack(padx=10,pady=10)
      
canvas.pack()
btn.pack(pady=20,padx=20)
      
frameA.place(relx=0.05,rely=0.01, relwidth=0.9,relheight=0.2)
frameB.place(relx=0.05,rely=0.25, relwidth=0.3,relheight=0.7)
frameC.place(relx=0.37,rely=0.25, relwidth=0.58,relheight=0.7)
      
btnB = Button(frameC,text="Yeni Kişi Ekle", command =  inputHandler,width=20,height=20,font=("Verdana 10 bold",20))
btnB.pack(pady=10,padx=20)


     
window.mainloop()
      