from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog
import os
import cv2
from time import strftime
from datetime import datetime



class FR:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x690+0+0")
        self.root.title("FACE RECOGNITION")
        
        
        img = Image.open(r"C:\Users\tahir\OneDrive\Desktop\AFR\college_images\FRW153.png")
        img = img.resize((1350,690),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)        
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1350,height=690)
        
        
        btn_FRW153 = Button(self.root,text="Recognize Face",command=self.face_recog,font=("arial",10,"bold"),height=1,width=30,bg="blue",fg="white")
        btn_FRW153.grid(row=3,column=6,padx=0,pady=0)
        btn_FRW153.place(x=550,y=510)


    #=======================att==============
    def mark_att(self,n,i,r,d):
        with open("Tahir.csv", "r+", newline="\n") as f:
            myDatalist=f.readlines()
            name_list = []
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if((n not in name_list) and (i not in name_list) and (r not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{n},{i},{r},{d},{dtString},{d1},Present")
            


    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,color,text,clf):
            gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor)
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="FirstProj153",database="afr")
                my_cursor = conn.cursor()
                
                
                my_cursor.execute("select Name from student where student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                
                my_cursor.execute("select Roll from student where student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                
                my_cursor.execute("select Dep from student where student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                
                my_cursor.execute("select student_id from student where student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                
                
                
                if confidence>77:
                    cv2.putText(img, f"Name: {n}",(x,y-100),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img, f"ID: {i}",(x,y-70),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img, f"Roll: {r}",(x,y-40),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img, f"Department: {d}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    self.mark_att(n, i, r, d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h), (0,0,255),3)
                    cv2.putText(img,"UNKNOWN",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)

                coord=[x,y,w,h]#####
            return coord
        
        def recognize(img,clf,faceCascade):
            #coord=draw_boundray(img, faceCascade, 1.1, (255,25,255), "Face", clf)##########
            coord=draw_boundray(img, faceCascade, 1.1, (255,25,255), "Face", clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(1)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img, clf, faceCascade)
            #img=recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)
            
            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
                
          
          
          
          
if __name__ == "__main__":
    root = Tk()
    obj = FR(root)
    root.mainloop()
    