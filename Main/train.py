from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter as tk
import mysql.connector
import cv2
import os 
import numpy as np




class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl= Label(self.root,text="Train Data Set",font=("times new roman",30,"bold"),bg="white",fg="darkred")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open(r"D:\Accademic Study\face_recog_pic\18a.jpg")
        img_top = img_top.resize((1530,325), Image.LANCZOS)         # Use Image.ANTIALIAS for resizing
        self.photoimg_top = ImageTk.PhotoImage(img_top)            # Convert the resized image to PhotoImage

        
        f_lbl = Label(self.root, image=self.photoimg_top)       # Display the image using Label widget
        f_lbl.place(x=0, y=45, width=1530, height=325) 

        # button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="tan",fg="darkred")
        b1_1.place(x=0,y=370,width=1530,height=60)

        img_bottom = Image.open(r"D:\Accademic Study\face_recog_pic\19a.jpg")
        img_bottom = img_bottom.resize((1530,325), Image.LANCZOS)         # Use Image.ANTIALIAS for resizing
        self.photoimg_bottom= ImageTk.PhotoImage(img_bottom)            # Convert the resized image to PhotoImage

        
        f_lbl = Label(self.root, image=self.photoimg_bottom)       # Display the image using Label widget
        f_lbl.place(x=0, y=430, width=1530, height=325) 


    def train_classifier(self):
        data_dir=("img data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  # Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Train",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)  

        #...............Train classifier and save........
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)                              
        clf.write("classifier.xml") 
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!!")





if __name__ == "__main__":
    root = tk.Tk()
    obj = Train(root)
    root.mainloop()        