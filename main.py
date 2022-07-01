from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog
import os
from student import Student
from help import Help
from developer import Developer
from train import Train
from face_recognition import FR
from attendance import Attendance
from about import About



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x690+0+0")
        self.root.title("Face Recognition System By TAHIR HABIB")
        
        
        #Header_img
        #img = Image.open(r"C:\Users\tahir\OneDrive\Desktop\AFR\college_images\153.png")
        #img = img.resize((1350,130),Image.ANTIALIAS)
        #self.photoimg=ImageTk.PhotoImage(img)        
        
        #f_lbl=Label(self.root,image=self.photoimg)
        #f_lbl.place(x=0,y=0,width=1350,height=130)
        
        
        #Background_img
        img_bg = Image.open(r"C:\Users\tahir\OneDrive\Desktop\AFR\college_images\1534.png")
        img_bg = img_bg.resize((1350,690),Image.ANTIALIAS)
        self.photoimg_bg=ImageTk.PhotoImage(img_bg)        
        
        bg_img=Label(self.root,image=self.photoimg_bg)
        bg_img.place(x=0,y=0,width=1350,height=690)
        
        #Main_title
        #title_lbl=Label(bg_img,text="Advance Face Recognition System",font=("Helvetica",25,"bold"),fg="grey",bg="navy")
        #title_lbl.place(x=0,y=0,width=1350,height=40)
        
        #____________________________________First Row Buttons_____________________________________________________
        
        #Student_Button_img
        std_btn_img = Image.open(r"C:\Users\tahir\OneDrive\Desktop\AFR\college_images\std153.png")
        std_btn_img = std_btn_img.resize((150,150),Image.ANTIALIAS)
        self.photoimg_std=ImageTk.PhotoImage(std_btn_img)
                
        std_img_btn=Button(bg_img,command=self.student_details,image=self.photoimg_std,cursor="hand2")
        std_img_btn.place(x=230,y=230,width=150,height=150)
        
        std_img_btn_down=Button(bg_img,command=self.student_details,text="Student Details",font=("arial",10,"bold"),width=16,bg="blue",fg="white",cursor="hand2")
        std_img_btn_down.place(x=230,y=350,width=150,height=30)
        
        
        
        #FD_Button_img
        FD_btn_img = Image.open(r"C:\Users\tahir\OneDrive\Desktop\AFR\college_images\fr153.png")
        FD_btn_img = FD_btn_img.resize((150,150),Image.ANTIALIAS)
        self.photoimg_FD=ImageTk.PhotoImage(FD_btn_img)
                
        FD_img_btn=Button(bg_img,command=self.fr_window,image=self.photoimg_FD,cursor="hand2")
        FD_img_btn.place(x=480,y=230,width=150,height=150)
        
        FD_img_btn_down=Button(bg_img,command=self.fr_window,text="Face Detection",font=("arial",10,"bold"),width=16,bg="blue",fg="white",cursor="hand2")
        FD_img_btn_down.place(x=480,y=350,width=150,height=30)
        
        
        
        #ATT_Button_img
        att_btn_img = Image.open(r"C:\Users\tahir\OneDrive\Desktop\AFR\college_images\att153.png")
        att_btn_img = att_btn_img.resize((150,150),Image.ANTIALIAS)
        self.photoimg_att=ImageTk.PhotoImage(att_btn_img)
                
        att_img_btn=Button(bg_img,command=self.att_window,image=self.photoimg_att,cursor="hand2")
        att_img_btn.place(x=730,y=230,width=150,height=150)
        
        att_img_btn_down=Button(bg_img,command=self.att_window,text="Attendence",font=("arial",10,"bold"),width=16,bg="blue",fg="white",cursor="hand2")
        att_img_btn_down.place(x=730,y=350,width=150,height=30)
        
        
        #help_Button_img
        help_btn_img = Image.open(r"C:\Users\tahir\OneDrive\Desktop\AFR\college_images\help153.png")
        help_btn_img = help_btn_img.resize((150,150),Image.ANTIALIAS)
        self.photoimg_help=ImageTk.PhotoImage(help_btn_img)
                
        help_img_btn=Button(bg_img,command=self.help_window,image=self.photoimg_help,cursor="hand2")
        help_img_btn.place(x=980,y=230,width=150,height=150)
        
        help_img_btn_down=Button(bg_img,text="Help",command=self.help_window,font=("arial",10,"bold"),width=16,bg="blue",fg="white",cursor="hand2")
        help_img_btn_down.place(x=980,y=350,width=150,height=30)
        
        #____________________________________Second Row Buttons_____________________________________________________ 
        
        
        
        #TrainData_Button_img
        train_btn_img = Image.open(r"C:\Users\tahir\OneDrive\Desktop\AFR\college_images\train153.png")
        train_btn_img = train_btn_img.resize((150,150),Image.ANTIALIAS)
        self.photoimg_train=ImageTk.PhotoImage(train_btn_img)
                
        train_img_btn=Button(bg_img,command=self.train_window,image=self.photoimg_train,cursor="hand2")
        train_img_btn.place(x=230,y=480,width=150,height=150)
        
        train_img_btn_down=Button(bg_img,command=self.train_window,text="Train Data",font=("arial",10,"bold"),width=16,bg="blue",fg="white",cursor="hand2")
        train_img_btn_down.place(x=230,y=600,width=150,height=30)
        
        
        
        #Photo_Button_img
        photo_btn_img = Image.open(r"C:\Users\tahir\OneDrive\Desktop\AFR\college_images\pics153.png")
        photo_btn_img = photo_btn_img.resize((150,150),Image.ANTIALIAS)
        self.photoimg_photo=ImageTk.PhotoImage(photo_btn_img)
                
        photo_img_btn=Button(bg_img,image=self.photoimg_photo,cursor="hand2",command=self.open_img)
        photo_img_btn.place(x=480,y=480,width=150,height=150)
        
        photo_img_btn_down=Button(bg_img,text="Photos",command=self.open_img,font=("arial",10,"bold"),width=16,bg="blue",fg="white",cursor="hand2")
        photo_img_btn_down.place(x=480,y=600,width=150,height=30)
        
        
        
        #Developer_Button_img
        deve_btn_img = Image.open(r"C:\Users\tahir\OneDrive\Desktop\AFR\college_images\dev153.png")
        deve_btn_img = deve_btn_img.resize((150,150),Image.ANTIALIAS)
        self.photoimg_deve=ImageTk.PhotoImage(deve_btn_img)
                
        deve_img_btn=Button(bg_img,command=self.developer_window,image=self.photoimg_deve,cursor="hand2")
        deve_img_btn.place(x=730,y=480,width=150,height=150)
        
        deve_img_btn_down=Button(bg_img,text="Developer",command=self.developer_window,font=("arial",10,"bold"),width=16,bg="blue",fg="white",cursor="hand2")
        deve_img_btn_down.place(x=730,y=600,width=150,height=30)
        
        
        
        #Exit_Button_img
        exit_btn_img = Image.open(r"C:\Users\tahir\OneDrive\Desktop\AFR\college_images\exit153.png")
        exit_btn_img = exit_btn_img.resize((150,150),Image.ANTIALIAS)
        self.photoimg_exit=ImageTk.PhotoImage(exit_btn_img)
                
        exit_img_btn=Button(bg_img,command=self.root.quit,image=self.photoimg_exit,cursor="hand2")
        exit_img_btn.place(x=980,y=480,width=150,height=150)
        
        exit_img_btn_down=Button(bg_img,text="Exit",command=self.root.quit,font=("arial",10,"bold"),width=16,bg="red",fg="white",cursor="hand2")
        exit_img_btn_down.place(x=980,y=600,width=150,height=30)
        
        #DISCRIPTION
        
        dis_btn_img = Image.open(r"C:\Users\tahir\OneDrive\Desktop\AFR\college_images\dis.png")
        dis_btn_img = dis_btn_img.resize((40,40),Image.ANTIALIAS)
        self.photoimg_about=ImageTk.PhotoImage(dis_btn_img)
                
        dis_img_btn=Button(bg_img,command=self.dis_window,image=self.photoimg_about,cursor="hand2")
        dis_img_btn.place(x=1270,y=610,width=40,height=40)
        

        #================ Functions Buttons ======================
    def open_img(self):
        os.startfile(r"C:\Users\tahir\OneDrive\Desktop\AFR\data")    
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Student(self.new_window)
            
        
        
    def help_window(self):
        self.new_window=Toplevel(self.root)
        self.app = Help(self.new_window)
        
        
        
    def developer_window(self):
        self.new_window=Toplevel(self.root)
        self.app = Developer(self.new_window)
    
    
    def train_window(self):
        self.new_window=Toplevel(self.root)
        self.app = Train(self.new_window)
    
    
    def fr_window(self):
        self.new_window=Toplevel(self.root)
        self.app = FR(self.new_window)
    
    
    def att_window(self):
        self.new_window=Toplevel(self.root)
        self.app = Attendance(self.new_window)
    
    
    
    def dis_window(self):
        self.new_window=Toplevel(self.root)
        self.app = About(self.new_window)
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    