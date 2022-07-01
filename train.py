from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog
import os
import cv2
import numpy as np



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x690+0+0")
        self.root.title("TRAIN DATA")
        
        
        img = Image.open(r"C:\Users\tahir\OneDrive\Desktop\AFR\college_images\dataset153.png")
        img = img.resize((1350,690),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)        
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1350,height=690)
        
        
        btn_train_dataset = Button(self.root,command=self.train_classifier,text="Train Data Set",font=("arial",10,"bold"),height=1,width=30,bg="blue",fg="white")
        btn_train_dataset.grid(row=3,column=6,padx=0,pady=0)
        btn_train_dataset.place(x=550,y=565)



        
        
    def train_classifier(self):
        data_dir = r"C:\Users\tahir\OneDrive\Desktop\AFR\data"
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces = []
        ids = []
        
        
        for image in path:
            img=Image.open(image).convert("L")
            imageNP=np.array(img,"uint8")
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training", imageNP)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        
        #================== train and save ==============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write('classifier.xml')
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset Completed!!!")
                
          
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
    