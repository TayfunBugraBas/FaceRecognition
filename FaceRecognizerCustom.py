import cv2
import numpy as np
import face_recognition
import os
from tkinter import ttk
from tkinter import *


path = 'Images'
images = []
classNames = []
pictureName = 'NOT-IDENTIFIED'
anc ='D:\projects/Frecs/Images/'
aps = os.path.join('Images')

faceProto = "opencv_face_detector.pbtxt"
faceModel = "opencv_face_detector_uint8.pb"
ageProto = "age_deploy.prototxt"
ageModel = "age_net.caffemodel"
genderProto="gender_deploy.prototxt"
genderModel="gender_net.caffemodel"


MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)
ageList=['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList=['Erkek','Kadin']

faceNet=cv2.dnn.readNet(faceModel,faceProto)
ageNet=cv2.dnn.readNet(ageModel,ageProto)
genderNet=cv2.dnn.readNet(genderModel,genderProto)


class FRec:
   
   
    
   def __init__(self):
       
        pass
    
   btnChk1 = False
   btnChk2 = False 
   
   ROOT = Tk()
   
  
   
   def disable_event():
      pass
   
   def BtnNormalizer():
       FRec.btnChk1 = False
       FRec.btnChk2 = False 
    
   def BtnOneControl():
       FRec.btnChk1 = True
      
   def BtnTwoControl():     
       FRec.btnChk2 = True      
    
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
   ROOT.protocol("WM_DELETE_WINDOW",disable_event)
   ROOT.title("Control Panel")
   canvas = Canvas(ROOT,height=200,width=200)   
   LABEL = Label(ROOT, text="Yapacağınız işleme Dikkat Ediniz")
   LABEL.pack(padx=70)
   
   #
   def pictureTaker(x):
       pictureName =x+'.jpg'
       
       
       
      
       btn2 = Button(FRec.ROOT,text ="Kamerayı Kapat",command = FRec.BtnTwoControl)
       btn2.pack()
       
       
       btn1 = Button(FRec.ROOT,text ="Resim Çek",command = FRec.BtnOneControl)
       btn1.pack()
       
       cap2 = cv2.VideoCapture(0)
       while True:
           
          
           
           FRec.ROOT.update()
           ret2,frame2 = cap2.read()
           frame2 = frame2[120:120+250,200:200+250, :]     
           cv2.imshow('',frame2)
           if cv2.waitKey(1) & FRec.btnChk1 == True:
             
               cv2.imwrite(os.path.join(aps, 'app.jpg'),frame2)

               old_file = os.path.join("Images", "app.jpg")
               new_file = os.path.join("Images", pictureName)
               os.rename(old_file, new_file)
               btn1.destroy()
               btn2.destroy()
               FRec.BtnNormalizer()
               break
               
                   
               
               
               
           if cv2.waitKey(1) & FRec.btnChk2 == True:
             btn1.destroy()
             btn2.destroy()
             FRec.BtnNormalizer()  
             break
             
          
               
         
         
       cap2.release()
       cv2.destroyAllWindows()    
   

    #   
   def openCam():
       btn2 = Button(FRec.ROOT,text ="Kamerayı Kapat",command = FRec.BtnTwoControl)
       btn2.pack()
      
       
       cap = cv2.VideoCapture(0)
       encodeListKnown = FRec.findEncodings(images)
        
       while True:
           FRec.ROOT.update()
           
           
           success, frame = cap.read()
           frame = frame[120:120+400,200:200+400, :]
         
           imgS = cv2.resize(frame,(0,0),None,0.25,0.25)
           imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        
           facesCurFrame = face_recognition.face_locations(imgS)
           encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
           
           
           blob=cv2.dnn.blobFromImage(frame, 1.0, (227,227), MODEL_MEAN_VALUES, swapRB=False)
           genderNet.setInput(blob)
           genderPreds=genderNet.forward()
           gender=genderList[genderPreds[0].argmax()]
           
           
           ageNet.setInput(blob)
           agePreds=ageNet.forward()
           age=ageList[agePreds[0].argmax()]
           
           
           
        
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
                   cv2.putText(frame, f'{gender}, {age}', (x1-6,y2+60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2, cv2.LINE_AA)
               else:
                  name = 'NOT-IDENTIFIED'
                   
                  y1,x2,y2,x1 = faceLocation
                  y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                  cv2.rectangle(frame,(x1,y1-20),(x2,y2),(0,255,0),2)
                   
                  cv2.putText(frame,name,(x1-6,y2+30),cv2.FONT_ITALIC,1,(255,255,255),2)
                  cv2.putText(frame, f'{gender}, {age}', (x1-6,y2+60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2, cv2.LINE_AA)
                  
           
        
           cv2.imshow('',frame)
           if cv2.waitKey(1) & FRec.btnChk2 == True:
             btn2.destroy()  
             FRec.BtnNormalizer()  
             break
           
       cap.release()
       cv2.destroyAllWindows()    
       
       
      
   
