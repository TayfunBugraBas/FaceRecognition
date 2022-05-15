from tkinter import *
from FaceRecognizerCustom import FRec
from tkinter import ttk
import threading

class AppMain:
    

    
 def __init__(self):
        pass
    
 def destroyer():
     FRec.ROOT.destroy()   
        
 def faceRecognizerOpener():
     FRec.openCam()        
 
 def inputTaker(z):
     a=z
     threading.Thread(target=FRec.pictureTaker(a)).start()
 def Disable():
     pass

     
