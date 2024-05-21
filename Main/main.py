from tkinter import*
from tkinter import Label,Button
from PIL import Image, ImageTk
import tkinter as tk
from student_buttonn import Student
import os 
from train import Train
from face_recognition import Face_Recognition





class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # (adding 1st image ) Load and resize the image using PIL
        img_path = r"D:\Accademic Study\face_recog_pic\face-recognition-attendance-system.jpg" 
        img = Image.open(img_path)
        img = img.resize((450,150), Image.LANCZOS)     # Use Image.ANTIALIAS for resizing
        self.photoimg = ImageTk.PhotoImage(img)        # Convert the resized image to PhotoImage

        
        f_lb1 = Label(self.root, image=self.photoimg)  # Display the image using Label widget
        f_lb1.place(x=0, y=0, width=450, height=150)



        # (adding 2nd image ) Load and resize the image using PIL
        img_path1 = r"D:\Accademic Study\face_recog_pic\depositphotos_644063982-stock-photo-student-cartoon-studying-front-computer.jpg" 
        img1 = Image.open(img_path1)
        img1 = img1.resize((600,150), Image.LANCZOS)         # Use Image.ANTIALIAS for resizing
        self.photoimg1 = ImageTk.PhotoImage(img1)            # Convert the resized image to PhotoImage

        
        f_lb1 = Label(self.root, image=self.photoimg1)       # Display the image using Label widget
        f_lb1.place(x=450, y=0, width=600, height=150)



        # (adding 3rd image ) Load and resize the image using PIL
        img_path2 = r"D:\Accademic Study\face_recog_pic\attendance-text-written-education-background-back-to-school-concept-banner-sketch-supplies-pencils-over-classroom-d-157634154.webp"
        img2 = Image.open(img_path2)
        img2 = img2.resize((480,150), Image.LANCZOS)         # Use Image.ANTIALIAS for resizing
        self.photoimg2 = ImageTk.PhotoImage(img2)            # Convert the resized image to PhotoImage

        
        f_lb1 = Label(self.root, image=self.photoimg2)       # Display the image using Label widget
        f_lb1.place(x=1050, y=0, width=480, height=150)   



        # background image
        img3 = Image.open(r"D:\Accademic Study\face_recog_pic\Guysfromandromeda Wp Content Uploads Galaxy.jpg")
        img3 = img3.resize((1530,790), Image.LANCZOS)         # Use Image.ANTIALIAS for resizing
        self.photoimg3 = ImageTk.PhotoImage(img3)            # Convert the resized image to PhotoImage

        
        bg_img = Label(self.root, image=self.photoimg3)       # Display the image using Label widget
        bg_img.place(x=0, y=130, width=1530, height=790)

        title_lbl= Label(bg_img,text="Face Recognition Attendance System",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        # student button
        img4 = Image.open(r"D:\Accademic Study\face_recog_pic\3a.png")
        img4 = img4.resize((220,220), Image.LANCZOS)         # Use Image.ANTIALIAS for resizing
        self.photoimg4 = ImageTk.PhotoImage(img4) 

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Students Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="tan",fg="red")
        b1_1.place(x=200,y=300,width=220,height=40)


        # Detect Face button
        img5 = Image.open(r"D:\Accademic Study\face_recog_pic\6a.gif")
        img5 = img5.resize((220,220), Image.LANCZOS)         # Use Image.ANTIALIAS for resizing
        self.photoimg5 = ImageTk.PhotoImage(img5) 

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="tan",fg="red")
        b1_1.place(x=500,y=300,width=220,height=40)



        # Attendance button
        img6 = Image.open(r"D:\Accademic Study\face_recog_pic\7a.webp")
        img6 = img6.resize((220,220), Image.LANCZOS)         # Use Image.ANTIALIAS for resizing
        self.photoimg6 = ImageTk.PhotoImage(img6) 

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="tan",fg="red")
        b1_1.place(x=800,y=300,width=220,height=40)



        # Help button
        img7 = Image.open(r"D:\Accademic Study\face_recog_pic\8a.jpg")
        img7 = img7.resize((220,220), Image.LANCZOS)         # Use Image.ANTIALIAS for resizing
        self.photoimg7 = ImageTk.PhotoImage(img7) 

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help",cursor="hand2",font=("times new roman",15,"bold"),bg="tan",fg="red")
        b1_1.place(x=1100,y=300,width=220,height=40)



        # train button
        img8 = Image.open(r"D:\Accademic Study\face_recog_pic\23a.png")
        img8 = img8.resize((220,220), Image.LANCZOS)         # Use Image.ANTIALIAS for resizing
        self.photoimg8 = ImageTk.PhotoImage(img8) 

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="tan",fg="red")
        b1_1.place(x=200,y=580,width=220,height=40)



        # Photos button
        img9 = Image.open(r"D:\Accademic Study\face_recog_pic\17a.jpg")
        img9 = img9.resize((220,220), Image.LANCZOS)         # Use Image.ANTIALIAS for resizing
        self.photoimg9 = ImageTk.PhotoImage(img9) 

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="tan",fg="red")
        b1_1.place(x=500,y=580,width=220,height=40)


        # Developer button
        img10 = Image.open(r"D:\Accademic Study\face_recog_pic\6a.gif")
        img10 = img10.resize((220,220), Image.LANCZOS)         # Use Image.ANTIALIAS for resizing
        self.photoimg10 = ImageTk.PhotoImage(img10) 

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="tan",fg="red")
        b1_1.place(x=800,y=580,width=220,height=40)


        # Exit button
        img11 = Image.open(r"D:\Accademic Study\face_recog_pic\26a.jpg")
        img11 = img11.resize((220,220), Image.LANCZOS)         # Use Image.ANTIALIAS for resizing
        self.photoimg11 = ImageTk.PhotoImage(img11) 

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="tan",fg="red")
        b1_1.place(x=800,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("img data")    



    #.......... Function button............
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)   


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)      
        

    



      


if __name__ == "__main__":
    root = tk.Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
