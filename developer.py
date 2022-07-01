from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
import os


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x690+0+0")
        self.root.title("Developer")
        
        
        
        img = Image.open(r"C:\Users\tahir\OneDrive\Desktop\AFR\college_images\deve153.png") 
        img = img.resize((1350,690),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        main_img=Label(self.root,image=self.photoimg,bd=2,relief=RIDGE)
        main_img.place(x=0,y=0,width=1350,height=690)
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()