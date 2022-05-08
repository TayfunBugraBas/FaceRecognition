import cv2
import numpy as np
import face_recognition
import os
from tkinter import ttk
from PIL import Image
import PIL


path = 'Images'
images = []
classNames = []
pictureName = 'NOT-IDENTIFIED'
anc ='D:\projects/Frecs/Images/'
aps = os.path.join('Images')



class FRec:
   def __init__(self):
       
        pass
    
         
   
       
         
   def findEncodings(images):
       myList = os.listdir(path)
       
       for cl in myList:
           curImg = cv2.imread(f'{path}/{cl}')
           images.append(curImg)
           classNames.append(os.path.splitext(cl)[0])
       
       encodedList = []
       for img in images:
           img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
           encodedImg = face_recognition.face_encodings(img)[0]
           encodedList.append(encodedImg)
       return encodedList 
   
   #
   def pictureTaker(x):
       pictureName =x+'.jpg'
       
       
       cap2 = cv2.VideoCapture(0)
       while True:
           ret2,frame2 = cap2.read()
           frame2 = frame2[120:120+250,200:200+250, :]     
           cv2.imshow('',frame2)
           if cv2.waitKey(20) & 0xFF == ord('a'):
             
               cv2.imwrite(os.path.join(aps, 'app.jpg'),frame2)

               old_file = os.path.join("Images", "app.jpg")
               new_file = os.path.join("Images", pictureName)
               os.rename(old_file, new_file)
               break
                   
               
               
               
           if cv2.waitKey(20) & 0XFF == ord('q'):
             break
          
               
         
         
       cap2.release()
       cv2.destroyAllWindows()    
   

    #   
   def openCam():
       
      
       
       cap = cv2.VideoCapture(0)
       encodeListKnown = FRec.findEncodings(images)
        
       while True:
           success, frame = cap.read()
           frame = frame[120:120+300,200:200+300, :]
         
           imgS = cv2.resize(frame,(0,0),None,0.25,0.25)
           imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        
           facesCurFrame = face_recognition.face_locations(imgS)
           encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
        
           for encodeFace,faceLocation in zip(encodesCurFrame,facesCurFrame):
               Uyum = face_recognition.compare_faces(encodeListKnown,encodeFace)
               Benzerlik = face_recognition.face_distance(encodeListKnown,encodeFace)
               
               
              
               matchIndex = np.argmin(Benzerlik)
        
               if Uyum[matchIndex]:
                   name = classNames[matchIndex].upper()
                   
                   y1,x2,y2,x1 = faceLocation
                   y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                   cv2.rectangle(frame,(x1,y1-20),(x2,y2),(0,255,0),2)
                   
                   cv2.putText(frame,name,(x1-6,y2+30),cv2.FONT_ITALIC,1,(255,255,255),2)
               else:
                  name = 'NOT-IDENTIFIED'
                   
                  y1,x2,y2,x1 = faceLocation
                  y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                  cv2.rectangle(frame,(x1,y1-20),(x2,y2),(0,255,0),2)
                   
                  cv2.putText(frame,name,(x1-6,y2+30),cv2.FONT_ITALIC,1,(255,255,255),2)
        
           cv2.imshow('',frame)
           if cv2.waitKey(1) & 0xFF == ord('q'):
               break
           
       cap.release()
       cv2.destroyAllWindows()    
       
       
      
   
