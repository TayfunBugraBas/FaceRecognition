from tkinter import *
from FaceRecognizerCustom import FRec
from tkinter import ttk


class AppMain:
    

    
 def __init__(self):
        pass
        
 def faceRecognizerOpener():
     FRec.openCam()        
 
 def inputTaker(z):
     a=z
     FRec.pictureTaker(a)
