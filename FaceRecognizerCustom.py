import cv2
import numpy as np
import face_recognition
import os

path = 'Images'
images = []
classNames = []
myList = os.listdir(path)

class FRec:
   def __init__(self):
       
        pass
    
    
   for cl in myList:
       curImg = cv2.imread(f'{path}/{cl}')
       images.append(curImg)
       classNames.append(os.path.splitext(cl)[0])
       
   def findEncodings(images):
       encodedList = []
       for img in images:
           img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
           encodedImg = face_recognition.face_encodings(img)[0]
           encodedList.append(encodedImg)
       return encodedList 
   
   encodeListKnown = findEncodings(images)

   
   def openCam():
       
      
       
       cap = cv2.VideoCapture(0)
        
       while True:
           success, frame = cap.read()
           frame = frame[120:120+300,200:200+300, :]
         
           imgS = cv2.resize(frame,(0,0),None,0.25,0.25)
           imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        
           facesCurFrame = face_recognition.face_locations(imgS)
           encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
        
           for encodeFace,faceLocation in zip(encodesCurFrame,facesCurFrame):
               Uyum = face_recognition.compare_faces(FRec.encodeListKnown,encodeFace)
               Benzerlik = face_recognition.face_distance(FRec.encodeListKnown,encodeFace)
               
              
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
   
