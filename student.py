from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog
import os
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x690+0+0")
        self.root.title("STUDENT DETAILS")
           
        #variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1 = StringVar()
  
        #Main image
        
        #img = Image.open(r"college_images\main.png") 
        img = Image.open(r"C:\Users\tahir\OneDrive\Desktop\AFR\college_images\main153.png") 
        img = img.resize((1350,160),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        main_img=Label(self.root,image=self.photoimg,bd=2,relief=RIDGE)
        main_img.place(x=0,y=0,width=1350,height=140)
        
 
        #background image
        img_4 = Image.open(r"C:\Users\tahir\OneDrive\Desktop\AFR\college_images\590.png") 
        img_4 = img_4.resize((450,160),Image.ANTIALIAS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)
        
        bg_lbl=Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=140,width=1350,height=690)
 
        lbl_title = Label(bg_lbl,text="Connected with MySQL Database",font=("Helvetica",25,"bold"),fg="grey")
        lbl_title.place(x=0,y=0,width=1350,height=40)
        
        
        
        #Main working frame
        Manage_frame = Frame(bg_lbl,bd=2,relief=RIDGE,bg="dodgerblue4")
        Manage_frame.place(x=20,y=41,width=1305,height=500)
        
        #left frame
        DataLeftFrame = LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student data input",font=("times new roman",12,"bold"),fg="red")
        DataLeftFrame.place(x=10,y=10,width=600,height=480)
        
        img_left_frame = Image.open(r"C:\Users\tahir\OneDrive\Desktop\AFR\college_images\590153.png") #############################################
        img_left_frame = img_left_frame.resize((590,80),Image.ANTIALIAS)
        self.photoimg_4=ImageTk.PhotoImage(img_left_frame)
        
        left_pic=Label(DataLeftFrame,image=self.photoimg_4,bd=2,relief=RIDGE)
        left_pic.place(x=0,y=0,width=590,height=80)
        
        
        #Current course data frame
        Current_course_frame = LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Current course frame",font=("times new roman",12,"bold"),fg="red")
        Current_course_frame.place(x=0,y=85,width=590,height=100)
        
        #depart_labels
        lbl_dep = Label(Current_course_frame,text="Department",font=("arial",10,"bold"))
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)
        
        combo_dep=ttk.Combobox(Current_course_frame,textvariable=self.var_dep,font=("arial",10,"bold"),width=17,state="readonly")
        combo_dep["value"]=("select department","AI","CS","IT")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
       
       
        #course_labels
        lbl_dep = Label(Current_course_frame,text="Course",font=("arial",10,"bold"))
        lbl_dep.grid(row=0,column=2,padx=2,pady=10,sticky=W)
        
        combo_dep=ttk.Combobox(Current_course_frame,textvariable=self.var_course,font=("arial",10,"bold"),width=17,state="readonly")
        combo_dep["value"]=("select course","Course1","Course2","Course2","Course4")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        
        
        #Year_labels
        lbl_dep = Label(Current_course_frame,text="Year",font=("arial",10,"bold"))
        lbl_dep.grid(row=1,column=0,sticky=W,padx=2,pady=10)
        
        combo_dep=ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("arial",10,"bold"),width=17,state="readonly")
        combo_dep["value"]=("select year","2019","2020","2021","2022")
        combo_dep.current(0)
        combo_dep.grid(row=1,column=1,padx=2,sticky=W)
       
       
       
        #semeter_labels
        lbl_dep = Label(Current_course_frame,text="Semester",font=("arial",10,"bold"))
        lbl_dep.grid(row=1,column=2,padx=2,pady=10,sticky=W)
        
        combo_dep=ttk.Combobox(Current_course_frame,textvariable=self.var_semester,font=("arial",10,"bold"),width=17,state="readonly")
        combo_dep["value"]=("select department","Semester-1","Semester-2","Semester-3","Semester-4")
        combo_dep.current(0)
        combo_dep.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        
        
        #Student_datainfo data frame
        Student_datainfo_frame = LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Student Data",font=("times new roman",12,"bold"),fg="red")
        Student_datainfo_frame.place(x=0,y=190,width=590,height=260)
        
        
        #ID
        lbl_std_id = Label(Student_datainfo_frame,text="Student ID",font=("arial",10,"bold"))
        lbl_std_id.grid(row=0,column=0,sticky=W,padx=2,pady=7)
        
        std_id_entry=ttk.Entry(Student_datainfo_frame,textvariable=self.var_std_id,font=("arial",10,"bold"),width=22)
        std_id_entry.grid(row=0,column=1,sticky=W,padx=2,pady=7)
        
        
        #Name
        lbl_std_name = Label(Student_datainfo_frame,text="Student Name",font=("arial",10,"bold"))
        lbl_std_name.grid(row=0,column=2,sticky=W,padx=2,pady=7)
        
        std_name_entry=ttk.Entry(Student_datainfo_frame,textvariable=self.var_std_name,font=("arial",10,"bold"),width=22)
        std_name_entry.grid(row=0,column=3,sticky=W,padx=2,pady=7)
        
        
        #Division
        lbl_class_division = Label(Student_datainfo_frame,text="Class Division",font=("arial",10,"bold"))
        lbl_class_division.grid(row=1,column=0,sticky=W,padx=2,pady=7)
        
        combo_div=ttk.Combobox(Student_datainfo_frame,textvariable=self.var_div,font=("arial",10),width=18,state="readonly")
        combo_div["value"]=("select Division","A","B","C")
        combo_div.current(0)
        combo_div.grid(row=1,column=1,padx=2,pady=7,sticky=W)
        
        
        #Roll
        lbl_roll = Label(Student_datainfo_frame,text="Student Roll no.",font=("arial",10,"bold"))
        lbl_roll.grid(row=1,column=2,sticky=W,padx=2,pady=7)
        
        std_roll_entry=ttk.Entry(Student_datainfo_frame,textvariable=self.var_roll,font=("arial",10,"bold"),width=22)
        std_roll_entry.grid(row=1,column=3,sticky=W,padx=2,pady=7)
        
        
        #Gender
        lbl_gender = Label(Student_datainfo_frame,text="Gender",font=("arial",10,"bold"))
        lbl_gender.grid(row=2,column=0,sticky=W,padx=2,pady=7)
        
        combo_gender=ttk.Combobox(Student_datainfo_frame,textvariable=self.var_gender,font=("arial",10),width=18,state="readonly")
        combo_gender["value"]=("select Gender","Male","Female")
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1,padx=2,pady=7,sticky=W)
        
        
        #DOB
        lbl_std_DOB = Label(Student_datainfo_frame,text="Student DOB",font=("arial",10,"bold"))
        lbl_std_DOB.grid(row=2,column=2,sticky=W,padx=2,pady=7)
        
        std_DOB_entry=ttk.Entry(Student_datainfo_frame,textvariable=self.var_dob,font=("arial",10,"bold"),width=22)
        std_DOB_entry.grid(row=2,column=3,sticky=W,padx=2,pady=7)
        
        
        #Email
        lbl_std_email = Label(Student_datainfo_frame,text="Student email",font=("arial",10,"bold"))
        lbl_std_email.grid(row=3,column=0,sticky=W,padx=2,pady=7)
        
        std_email_entry=ttk.Entry(Student_datainfo_frame,textvariable=self.var_email,font=("arial",10,"bold"),width=22)
        std_email_entry.grid(row=3,column=1,sticky=W,padx=2,pady=7)
        
        
        #Phone
        lbl_std_phone = Label(Student_datainfo_frame,text="Student Phone",font=("arial",10,"bold"))
        lbl_std_phone.grid(row=3,column=2,sticky=W,padx=2,pady=7)
        
        std_phone_entry=ttk.Entry(Student_datainfo_frame,textvariable=self.var_phone,font=("arial",10,"bold"),width=22)
        std_phone_entry.grid(row=3,column=3,sticky=W,padx=2,pady=7)
        
        
        #Address
        lbl_std_address = Label(Student_datainfo_frame,text="Student Address",font=("arial",10,"bold"))
        lbl_std_address.grid(row=4,column=0,sticky=W,padx=2,pady=7)
        
        std_address_entry=ttk.Entry(Student_datainfo_frame,textvariable=self.var_address,font=("arial",10,"bold"),width=22)
        std_address_entry.grid(row=4,column=1,sticky=W,padx=2,pady=7)
        
        
        #Teacher
        lbl_std_teacher = Label(Student_datainfo_frame,text="Teacher",font=("arial",10,"bold"))
        lbl_std_teacher.grid(row=4,column=2,sticky=W,padx=2,pady=7)
        
        std_teacher_entry=ttk.Entry(Student_datainfo_frame,textvariable=self.var_teacher,font=("arial",10,"bold"),width=22)
        std_teacher_entry.grid(row=4,column=3,sticky=W,padx=2,pady=7)
        
        
        #Radio_Button
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(Student_datainfo_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes" )
        radiobtn1.grid(row=6,column=0)
        
        
        radiobtn2 = ttk.Radiobutton(Student_datainfo_frame,variable=self.var_radio1,text="No Photo Sample",value="No" )
        radiobtn2.grid(row=6,column=1)
        
        
        #Button Frame
        Button_frame = Frame(DataLeftFrame,bd=2,relief=RIDGE,bg="snow")
        Button_frame.place(x=10,y=410,width=571,height=34)
        
        #Buttons
        btn_add = Button(Button_frame,text="Save",command=self.add_data,font=("arial",7,"bold"),width=10,bg="blue",fg="white")
        btn_add.grid(row=0,column=0,padx=2,pady=2)
        
        
        btn_update = Button(Button_frame,text="Update",command=self.update_data,font=("arial",7,"bold"),width=10,bg="blue",fg="white")
        btn_update.grid(row=0,column=2,padx=2,pady=2)
        
        
        btn_delete = Button(Button_frame,command=self.delete_data,text="Delete",font=("arial",7,"bold"),width=10,bg="blue",fg="white")
        btn_delete.grid(row=0,column=3,padx=2,pady=2)
        
        
        btn_reset = Button(Button_frame,command=self.reset_data,text="Reset",font=("arial",7,"bold"),width=10,bg="blue",fg="white")
        btn_reset.grid(row=0,column=4,padx=2,pady=2)
       
       
       
        btn_Take_Photo_Sample = Button(Button_frame,command=self.generate_dataset,text="Take Photo Sample",font=("arial",8,"bold"),width=16,bg="blue",fg="white")
        btn_Take_Photo_Sample.grid(row=0,column=5,padx=2,pady=2)
        
        
        btn_Update_Photo_Sample = Button(Button_frame,command=self.reset_data,text="Update Photo Sample",font=("arial",8,"bold"),width=17,bg="blue",fg="white")
        btn_Update_Photo_Sample.grid(row=0,column=6,padx=2,pady=2)
        

        
        
        #Right frame
        DataRightFrame = LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="red")
        DataRightFrame.place(x=620,y=10,width=670,height=480)
      
        
        #image
        img_right_frame = Image.open(r"C:\Users\tahir\OneDrive\Desktop\AFR\college_images\660153.png") ################################
        img_right_frame = img_right_frame.resize((660,80),Image.ANTIALIAS)
        self.photoimg_5=ImageTk.PhotoImage(img_right_frame)
        
        right_pic=Label(DataRightFrame,image=self.photoimg_5,bd=2,relief=RIDGE)
        right_pic.place(x=0,y=0,width=660,height=80)
        
        #search frame
        search_Frame = LabelFrame(DataRightFrame,bd=4,relief=RIDGE,padx=2,text="search student information",font=("times new roman",12,"bold"),fg="red")
        search_Frame.place(x=0,y=80,width=660,height=70)
        
        
        #search lbl
        lbl_search = Label(search_Frame,text="Search By",font=("arial",10,"bold"),fg="white",bg="red")
        lbl_search.grid(row=0,column=0,sticky=W,padx=2,pady=7)
        
        #search
        self.var_com_search = StringVar()
      
        
        combo_search=ttk.Combobox(search_Frame,textvariable=self.var_com_search,font=("arial",10),width=18,state="readonly")
        combo_search["value"]=("Phone")
        #combo_search["value"]=("select option","Roll no.","Phone","Student ID")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2,pady=7,sticky=W)
    
        
        self.var_search= StringVar()
        search_entry=ttk.Entry(search_Frame,textvariable=self.var_search,font=("arial",10,"bold"),width=22)
        search_entry.grid(row=0,column=2,sticky=W,padx=2,pady=7)
        
        
        btn_search = Button(search_Frame, command=self.search_data ,text="Search",font=("arial",10,"bold"),width=14,bg="blue",fg="white")
        btn_search.grid(row=0,column=3,padx=2,pady=7)
        
        
        btn_showall = Button(search_Frame,command=self.fetch_data,text="Show All",font=("arial",10,"bold"),width=14,bg="blue",fg="white")
        btn_showall.grid(row=0,column=4,padx=2,pady=7)
        
    
        # Table 
        table_frame = Frame(DataRightFrame,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=160,width=660,height=290)
     
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table= ttk.Treeview(table_frame,column=("department","course","year","semester","id","name","division","roll","gender","dob","email","phone","address","teacher","photo",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
   
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("department",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("division",text="Class Division")
        self.student_table.heading("roll",text="Roll no.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone no.")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher Name")
        self.student_table.heading("photo",text="PhotoSample")
        
        
        
        self.student_table["show"] = "headings"
        
    
        self.student_table.column("department",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("semester",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("division",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=130)

        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
  
  
        
    def add_data(self):
        if(self.var_dep.get()=="" or self.var_address.get()=="" or self.var_course.get()=="" or self.var_std_id.get()==""
            or self.var_div.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()==""
            or self.var_gender.get()=="" or self.var_roll.get()=="" or self.var_std_name.get()=="" or self.var_year.get()==""
            or self.var_teacher.get()==""):
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="FirstProj153",database="afr")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
  
  
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                    
                
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Succcess","Student has been added Successfully.",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


        
    #fetch data  
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="FirstProj153",database="afr")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data) !=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
 
 
    
    #get cursor 
    def get_cursor(self,event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content["values"]
        
 
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])
        
 
 
    
    #update
    def update_data(self):
        if(self.var_dep.get()=="" or self.var_address.get()=="" or self.var_course.get()=="" or self.var_std_id.get()==""
            or self.var_div.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()==""
            or self.var_gender.get()=="" or self.var_roll.get()=="" or self.var_std_name.get()=="" or self.var_year.get()==""
            or self.var_teacher.get()==""):
            messagebox.showerror("Error","All Fields Are Required")
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure to update this student data",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="FirstProj153",database="afr")
                    my_cursor = conn.cursor()  
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where student_id=%s",(
    
                    
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
       
                  
                    ))
                else:
                    if not update:
                        return  
                conn.commit()
                self.fetch_data()
                conn.close()
                
                messagebox.showinfo("Success","Student successfully updated",parent= self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)




    #delete
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required!")
        else:
            try:
                Delete=messagebox.askyesno("Delete","Warning! Are you sure to delete this student data?",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="FirstProj153",database="afr")
                    my_cursor = conn.cursor()
                    sql="delete from student  where student_id=%s"
                    value=(self.var_std_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Your Student's data has been Deleted Successfully.",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)                    




    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    
         



    #search
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","please select option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="FirstProj153",database="afr")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student where " +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                rows = my_cursor.fetchall()
                
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in  rows:
                        self.student_table.insert("",END,values=i)
                        
                        
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)    
                    




    #========= Generate Data set ==============
    def generate_dataset(self):
        if(self.var_dep.get()=="" or self.var_address.get()=="" or self.var_course.get()=="" or self.var_std_id.get()==""
            or self.var_div.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()==""
            or self.var_gender.get()=="" or self.var_roll.get()=="" or self.var_std_name.get()=="" or self.var_year.get()==""
            or self.var_teacher.get()==""):
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="FirstProj153",database="afr")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where student_id=%s",(
    
                    
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get() == id+1
       
                  
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()   
                
                #========= loading harcascade XML file ========
                face_classifier = cv2.CascadeClassifier("C:/Users/tahir/OneDrive/Desktop/AFR/haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #minimum neighbor = 5
                    
                    for (x,y,w,h) in faces:#yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                cap = cv2.VideoCapture(1)
                img_id = 0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face, str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face", face)
                    
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)                         
                
                

           
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
    