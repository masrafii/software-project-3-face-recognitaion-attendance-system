from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter as tk
import mysql.connector
import cv2   

 




class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #......Variables.......
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar() 
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        



        # (adding 1st image ) Load and resize the image using PIL
        img_path = r"D:\Accademic Study\face_recog_pic\11a.png"
        img = Image.open(img_path)
        img = img.resize((450,130), Image.LANCZOS)     # Use Image.ANTIALIAS for resizing
        self.photoimg = ImageTk.PhotoImage(img)        # Convert the resized image to PhotoImage

        
        f_lb1 = Label(self.root, image=self.photoimg)  # Display the image using Label widget
        f_lb1.place(x=0, y=0, width=450, height=130)



        # (adding 2nd image ) Load and resize the image using PIL
        img_path1 = r"D:\Accademic Study\face_recog_pic\12a.jpg"
        img1 = Image.open(img_path1)
        img1 = img1.resize((600,150), Image.LANCZOS)         # Use Image.ANTIALIAS for resizing
        self.photoimg1 = ImageTk.PhotoImage(img1)            # Convert the resized image to PhotoImage

        
        f_lb1 = Label(self.root, image=self.photoimg1)       # Display the image using Label widget
        f_lb1.place(x=450, y=0, width=600, height=150)



        # (adding 3rd image ) Load and resize the image using PIL
        img_path2 = r"D:\Accademic Study\face_recog_pic\13a.jpg"
        img2 = Image.open(img_path2)
        img2 = img2.resize((480,150), Image.LANCZOS)         # Use Image.ANTIALIAS for resizing
        self.photoimg2 = ImageTk.PhotoImage(img2)            # Convert the resized image to PhotoImage

        
        f_lb1 = Label(self.root, image=self.photoimg2)       # Display the image using Label widget
        f_lb1.place(x=1050, y=0, width=480, height=150)


         # background image
        img3 = Image.open(r"D:\Accademic Study\face_recog_pic\10a.jpg")
        img3 = img3.resize((1530,790), Image.LANCZOS)         # Use Image.ANTIALIAS for resizing
        self.photoimg3 = ImageTk.PhotoImage(img3)            # Convert the resized image to PhotoImage

        
        bg_img = Label(self.root, image=self.photoimg3)       # Display the image using Label widget
        bg_img.place(x=0, y=130, width=1530, height=790)

        title_lbl= Label(bg_img,text="Student Management System",font=("times new roman",30,"bold"),bg="white",fg="darkred")
        title_lbl.place(x=0,y=0,width=1530,height=45)   

        # Label frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=45,width=1530,height=790)

        # .....Left label frame 
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=740,height=580)

        img_left = Image.open(r"D:\Accademic Study\face_recog_pic\10a.jpg")
        img_left = img_left.resize((730,130), Image.LANCZOS)         # Use Image.ANTIALIAS for resizing
        self.photoimg_left = ImageTk.PhotoImage(img_left)            # Convert the resized image to PhotoImage

        
        f_lbl = Label(Left_frame, image=self.photoimg_left)       # Display the image using Label widget
        f_lbl.place(x=5, y=0, width=730, height=130)       # Convert the resized image to PhotoImage

        #....Current course  Information
        current_course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=15,y=160,width=730,height=120)

        # Department
        dep_label= Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="read only",width=17)
        dep_combo["values"]=("Select Department","CSE","EEE","NFE","Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Course
        course_label= Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="read only",width=17)
        course_combo["values"]=("Select Course","System","History of BD","Basic python","C fundamentals")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # year
        year_label= Label(current_course_frame,text="YEAR",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="read only",width=17)
        year_combo["values"]=("Select Year","1020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        semester_label= Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="read only",width=17)
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #....Class Student Information
        class_student_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=15,y=290,width=730,height=300)

        # student id
        student_id_label= Label(class_student_frame,text="Student ID",font=("times new roman",12,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=10,sticky=W)

        student_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("times new roman",13,"bold"))
        student_id_entry.grid(row=0,column=1,padx=10,sticky=W)

        # student Name
        studentName_label= Label(class_student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        # class Didision
        class_div_label= Label(class_student_frame,text="Student Division",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=2,pady=15,sticky=W)

        
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="read only",width=21)
        div_combo["values"]=("Rangpur","Dhaka","Khulna")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=15,sticky=W)

        # Roll No
        roll_no_label= Label(class_student_frame,text="Roll No",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender
        Gander_label= Label(class_student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        Gander_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="read only",width=21)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        # DOB
        dob_label= Label(class_student_frame,text="Dob",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Email
        email_label= Label(class_student_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # phone no
        phone_label= Label(class_student_frame,text="Phone No",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Address
        address_label= Label(class_student_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Teacher Name
        teacher_label= Label(class_student_frame,text="Teacher Name",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # radio button
        self.var_radio1=StringVar()
        radio_btn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radio_btn1.grid(row=6,column=0)

        
        radio_btn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radio_btn2.grid(row=6,column=1) 

        # button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=223,width=720,height=28)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update", command=self.update_data,width=19,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=19,command=self.delete_data,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=251,width=720,height=40)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=40,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=40,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        update_photo_btn.grid(row=0,column=1)





        # Right label frame 
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=760,y=10,width=740,height=580)

        img_right = Image.open(r"D:\Accademic Study\face_recog_pic\16a.png")
        img_right = img_right.resize((730,130), Image.LANCZOS)         # Use Image.ANTIALIAS for resizing
        self.photoimg_right= ImageTk.PhotoImage(img_right)            # Convert the resized image to PhotoImage

        
        f_lbl = Label(Right_frame, image=self.photoimg_right)       # Display the image using Label widget
        f_lbl.place(x=5, y=0, width=730, height=130)


        # .........Search frame..........
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=730,height=70)

        search_label= Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="darkgreen",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="read only",width=15)
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=14,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=14,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)


        # .........Table frame..........
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=730, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name","roll","gender", "div", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo Sample Status")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #.......Function Declearetion.......

    def add_data(self):
        
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
         try:
            conn=mysql.connector.connect(host="localhost",username="root",password="as.masrafi2.k",database="student_db")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                             self.var_dep.get(),
                                                                                             self.var_course.get(),
                                                                                             self.var_year.get(),
                                                                                             self.var_sem.get(),
                                                                                             self.var_id.get(),
                                                                                             self.var_name.get(),
                                                                                             self.var_roll.get(),
                                                                                             self.var_gender.get(),
                                                                                             self.var_div.get(),
                                                                                             #self.var_roll.get(),
                                                                                             #self.var_gender.get(),
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
            messagebox.showinfo("Success","Student details added successfully",parent=self.root)
         except Exception as es:
            messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root) 
    
    

    #..........fetch data.........
    def fetch_data(self):
       conn=mysql.connector.connect(host="localhost",username="root",password="as.masrafi2.k",database="student_db")
       my_cursor=conn.cursor()
       my_cursor.execute("Select * from student")
       data=my_cursor.fetchall()

       if len(data)!=0:
          self.student_table.delete(*self.student_table.get_children())
          for i in data:
             self.student_table.insert("",END,values=i)
          conn.commit()
       conn.close()  

    #........get cursor........
    def get_cursor(self,event=""):
       cursor_focus=self.student_table.focus()
       content=self.student_table.item(cursor_focus)
       data=content["values"]

       self.var_dep.set(data[0]),
       self.var_course.set(data[1]),
       self.var_year.set(data[2]),
       self.var_sem.set(data[3]),
       self.var_id.set(data[4]),
       self.var_name.set(data[5]),
       self.var_roll.set(data[6]),
       self.var_gender.set(data[7]),
       self.var_div.set(data[8]),
       #self.var_roll.set(data[7]),
       #self.var_gender.set(data[8]),
       self.var_dob.set(data[9]),
       self.var_email.set(data[10]),
       self.var_phone.set(data[11]),
       self.var_address.set(data[12]),
       self.var_teacher.set(data[13]),
       self.var_radio1.set(data[14]),


    #...........update function.........
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
          try:
             Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
             if Update > 0:
                 conn = mysql.connector.connect(host="localhost", username="root", password="as.masrafi2.k", database="student_db")
                 my_cursor = conn.cursor()
                 my_cursor.execute("UPDATE student SET Department=%s, Course=%s, Year=%s, Semester=%s, `Student ID`=%s, Name=%s, Roll=%s, Gender=%s, Division=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, `Photo Sample Status`=%s where `Student Id`=%s", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_div.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_id.get()
                     ))
                 conn.commit()
                 self.fetch_data()
                 conn.close()
                 messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
          except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)  


    #...... delete function.........
    def delete_data(self):
     if self.var_id.get() == "":
         messagebox.showerror("Error", "Student ID must be required", parent=self.root)
     else:
         try:
             delete = messagebox.askyesno("Student delete Page", "Do you want to delete this page", parent=self.root)
             if delete > 0:
                 conn = mysql.connector.connect(host="localhost", username="root", password="as.masrafi2.k", database="student_db")
                 my_cursor = conn.cursor()
                 sql = "delete from student where `Student ID`=%s"  # Corrected SQL query   # Id to ID lilkechi 17/5
                 val = (self.var_id.get(),)  # Corrected to get the value
                 my_cursor.execute(sql, val)
                 conn.commit()
                 self.fetch_data()
                 conn.close()
                 messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
         except Exception as es:
             messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)  


    #...........Reset data........
    def reset_data(self):
       self.var_dep.set("Select Department")
       self.var_course.set("Select Course")
       self.var_year.set("Select Year")
       self.var_sem.set("Select Semester")
       self.var_id.set("")
       self.var_name.set("")
       self.var_roll.set("")
       self.var_gender.set("Male")
       self.var_div.set("Select division")
       #self.var_roll.set("")
       #self.var_gender.set("Male")
       self.var_dob.set("")
       self.var_email.set("")
       self.var_phone.set("")
       self.var_address.set("")
       self.var_teacher.set("")
       self.var_radio1.set("")


    #...... Generate data set or take photo sample........
    def generate_dataset(self):
       if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
       else:
          try:
            conn = mysql.connector.connect(host="localhost", username="root", password="as.masrafi2.k", database="student_db")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            myresult=my_cursor.fetchall()
            id=0
            for x in myresult:
               id+=1
            my_cursor.execute("UPDATE student SET Department=%s, Course=%s, Year=%s, Semester=%s, `Student ID`=%s, Name=%s, Roll=%s, Gender=%s, Division=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, `Photo Sample Status`=%s WHERE `Student ID`=%s", (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_sem.get(),
                self.var_id.get(),
                self.var_name.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_div.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get(),
                self.var_id.get()
                   ))

            conn.commit()
            self.fetch_data()
            self.reset_data() 
            conn.close()

            #....... load pre-define data on face frontals from opencv...

            face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
               gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
               faces=face_classifier.detectMultiScale(gray,1.3,5)
               #scalling factor=1.3
               #minimum neighbor=5

               for(x,y,w,h) in faces:
                  face_cropped=img[y:y+h,x:x+w]
                  return face_cropped
               
            cap=cv2.VideoCapture(0) 
            img_id=0
            while True:
               ret,my_frame=cap.read()
               if face_cropped(my_frame) is not None: 
                  img_id+=1
                  face=cv2.resize(face_cropped(my_frame),(450,450)) 
                  face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                  file_name_path="img data/user"+str(id)+"."+str(img_id)+".jpg"
                  cv2.imwrite(file_name_path,face)
                  cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                  cv2.imshow("Crooped Face",face)

               if cv2.waitKey(1)==13 or int(img_id)==20:
                  break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Generating data sets compled!!!!",parent=self.root) 
          except Exception as es:
             messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)    



               
            
                                                                                                                                                                                                                             


if __name__ == "__main__":
    root = tk.Tk()
    obj = Student(root)
    root.mainloop()
