from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog
import os
import cv2
import csv



mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x690+0+0")
        self.root.title("Attendance")
        
        
        #=========variable==============
        self.var_att_id=StringVar()
        self.var_att_roll=StringVar()
        self.var_att_name=StringVar()
        self.var_att_dep=StringVar()
        self.var_att_time=StringVar()
        self.var_att_date=StringVar()
        self.var_att_attendance=StringVar()
        
        
        
        
        img = Image.open(r"C:\Users\tahir\OneDrive\Desktop\AFR\college_images\153att.png") 
        img = img.resize((1350,160),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        main_img=Label(self.root,image=self.photoimg,bd=2,relief=RIDGE)
        main_img.place(x=0,y=0,width=1350,height=160)
        
        #main frame
        Manage_frame = Frame(self.root,bd=2,relief=RIDGE,bg="dodgerblue4")
        Manage_frame.place(x=15,y=170,width=1320,height=510)
        
        #left frame
        DataLeftFrame = LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Attendance Details",font=("times new roman",12,"bold"),fg="black")
        DataLeftFrame.place(x=10,y=10,width=600,height=490)
        
        img_left_frame = Image.open(r"C:\Users\tahir\OneDrive\Desktop\AFR\college_images\att_detail.png") #############################################
        img_left_frame = img_left_frame.resize((590,80),Image.ANTIALIAS)
        self.photoimg_4=ImageTk.PhotoImage(img_left_frame)
        
        left_pic=Label(DataLeftFrame,image=self.photoimg_4,bd=2,relief=RIDGE)
        left_pic.place(x=0,y=0,width=590,height=80)
        
        #left inside
        Left_inside_frame = Frame(DataLeftFrame,bd=2,relief=RIDGE)
        Left_inside_frame.place(x=0,y=85,width=590,height=200)
        
        #Label and entries
        #ID_att
        name = Label(Left_inside_frame,text="Attendance ID:",font=("arial",10,"bold"))
        name.grid(row=0,column=0,sticky=W,padx=2,pady=7)
        
        name_entry=ttk.Entry(Left_inside_frame,textvariable=self.var_att_name,font=("arial",10,"bold"),width=22)
        name_entry.grid(row=0,column=1,sticky=W,padx=2,pady=7)
        
        #Name
        id_att = Label(Left_inside_frame,text="Name:",font=("arial",10,"bold"))
        id_att.grid(row=0,column=2,sticky=W,padx=2,pady=7)
        
        id_entry=ttk.Entry(Left_inside_frame,textvariable=self.var_att_id,font=("arial",10,"bold"),width=22)
        id_entry.grid(row=0,column=3,sticky=W,padx=2,pady=7)
        
        # Date
        Date = Label(Left_inside_frame,text="Date:",font=("arial",10,"bold"))
        Date.grid(row=1,column=0,sticky=W,padx=2,pady=7)
        
        Date_entry=ttk.Entry(Left_inside_frame,textvariable=self.var_att_date,font=("arial",10,"bold"),width=22)
        Date_entry.grid(row=1,column=1,sticky=W,padx=2,pady=7)
         
        #Department
        depart = Label(Left_inside_frame,text="Depart:",font=("arial",10,"bold"))
        depart.grid(row=1,column=2,sticky=W,padx=2,pady=7)
        
        depart_entry=ttk.Entry(Left_inside_frame,textvariable=self.var_att_dep,font=("arial",10,"bold"),width=22)
        depart_entry.grid(row=1,column=3,sticky=W,padx=2,pady=7)
    
        #Time
        time = Label(Left_inside_frame,text="Time:",font=("arial",10,"bold"))
        time.grid(row=2,column=0,sticky=W,padx=2,pady=7)
        
        time_entry=ttk.Entry(Left_inside_frame,textvariable=self.var_att_time,font=("arial",10,"bold"),width=22)
        time_entry.grid(row=2,column=1,sticky=W,padx=2,pady=7)
        
        
        #Roll
        Date = Label(Left_inside_frame,text="Roll:",font=("arial",10,"bold"))
        Date.grid(row=2,column=2,sticky=W,padx=2,pady=7)
        
        Date_entry=ttk.Entry(Left_inside_frame,textvariable=self.var_att_roll,font=("arial",10,"bold"),width=22)
        Date_entry.grid(row=2,column=3,sticky=W,padx=2,pady=7)
        
        #Att
        date = Label(Left_inside_frame,text="Attendance Status:",font=("arial",10,"bold"))
        date.grid(row=3,column=0,sticky=W,padx=2,pady=7)
        
        self.att_status=ttk.Combobox(Left_inside_frame,textvariable=self.var_att_attendance,width=20,font=("arial",10,'bold'),state="readonly")
        self.att_status["values"]=("Status","Present","Absent")
        self.att_status.grid(row=3,column=1)
        self.att_status.current(0)
        
        
        #Button Frame
        Button_frame = Frame(DataLeftFrame,bd=2,relief=RIDGE,bg="snow")
        Button_frame.place(x=10,y=290,width=571,height=57)
        
        #Buttons
        Import_CSV = Button(Button_frame,text="Import CSV",command=self.import_Csv,font=("arial",12,"bold"),height=1,width=17,bg="blue",fg="white")
        Import_CSV.grid(row=0,column=0,padx=2,pady=10)
        
        
        Export_CSV = Button(Button_frame,text="ExportCSV",command=self.exportCsv,font=("arial",12,"bold"),height=1,width=17,bg="blue",fg="white")
        Export_CSV.grid(row=0,column=2,padx=2,pady=10)
        
        
        #btn_Update = Button(Button_frame,text="Update",font=("arial",12,"bold"),height=1,width=13,bg="blue",fg="white")
        #btn_Update.grid(row=0,column=3,padx=2,pady=10)
        
        
        btn_reset = Button(Button_frame,text="Reset",command=self.reset_data,font=("arial",12,"bold"),height=1,width=18,bg="blue",fg="white")
        btn_reset.grid(row=0,column=4,padx=2,pady=10)
       
       
        down_img = Image.open(r"C:\Users\tahir\OneDrive\Desktop\AFR\college_images\downpic.png") #############################################
        down_img = down_img.resize((590,110),Image.ANTIALIAS)
        self.photoimg_5=ImageTk.PhotoImage(down_img)
        
        down_pic=Label(DataLeftFrame,image=self.photoimg_5,bd=2,relief=RIDGE)
        down_pic.place(x=0,y=350,width=590,height=110)
        
        #Right frame
        DataRightFrame = LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Attendance",font=("times new roman",12,"bold"),fg="black")
        DataRightFrame.place(x=620,y=10,width=685,height=490)
        
        #inside scroll bar frame
        Scroll_frame = Frame(DataRightFrame,bd=2,relief=RIDGE,bg="snow")
        Scroll_frame.place(x=5,y=5,width=660,height=450)
        
        scroll_x = ttk.Scrollbar(Scroll_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Scroll_frame,orient=VERTICAL)
        self.Att_report_table= ttk.Treeview(Scroll_frame,column=("name","roll","id","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Att_report_table.xview)
        scroll_y.config(command=self.Att_report_table.yview)
        
        self.Att_report_table.heading("id",text="Attandence ID")
        self.Att_report_table.heading("roll",text="Roll")
        self.Att_report_table.heading("name",text="Name")
        self.Att_report_table.heading("department",text="Department")
        self.Att_report_table.heading("time",text="Time")
        self.Att_report_table.heading("date",text="Date")
        self.Att_report_table.heading("attendance",text="Attendance")

        
        self.Att_report_table["show"] = "headings"
        
        self.Att_report_table.column("id",width=100)
        self.Att_report_table.column("roll",width=100)
        self.Att_report_table.column("name",width=100)
        self.Att_report_table.column("department",width=100)
        self.Att_report_table.column("time",width=100)
        self.Att_report_table.column("date",width=100)
        self.Att_report_table.column("attendance",width=100)
        
        self.Att_report_table.pack(fill=BOTH,expand=1)
        
        self.Att_report_table.bind("<ButtonRelease>",self.get_coursor)
        
        
        #========================== fetch data===================
        
    def fetchData(self,rows):
        self.Att_report_table.delete(*self.Att_report_table.get_children())
        for i in rows:
            self.Att_report_table.insert("",END,values=i)
                
    def import_Csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.")),parent=self.root)

        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                    mydata.append(i)
            self.fetchData(mydata)     
            
            
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to export.",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",") 
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
            
    
    def get_coursor(self,event=""):
        cursor_row = self.Att_report_table.focus()
        content = self.Att_report_table.item(cursor_row)
        rows = content['values']
        self.var_att_id.set(rows[0])                            
        self.var_att_roll.set(rows[1])                            
        self.var_att_name.set(rows[2])                            
        self.var_att_dep.set(rows[3])                            
        self.var_att_time.set(rows[4])                            
        self.var_att_date.set(rows[5])                            
        self.var_att_attendance.set(rows[6])
        
    
    def reset_data(self):
        self.var_att_id.set("")                            
        self.var_att_roll.set("")                            
        self.var_att_name.set("")                            
        self.var_att_dep.set("")                            
        self.var_att_time.set("")                            
        self.var_att_date.set("")                            
        self.var_att_attendance.set("")
                                      
            
     
        
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()