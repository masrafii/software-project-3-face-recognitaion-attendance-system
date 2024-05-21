from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import numpy as np
import mysql.connector
import time

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl= Label(self.root, text="FACE RECOGNITION", font=("times new roman", 30, "bold"), bg="tan", fg="darkred") 
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # First image
        img_top = Image.open("D:/Accademic Study/face_recog_pic/18a.jpg")
        img_top = img_top.resize((500, 740), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=500, height=740)

        # Second image
        img_bottom = Image.open("D:/Accademic Study/face_recog_pic/29a.webp")
        img_bottom = img_bottom.resize((1050, 740), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=500, y=45, width=1050, height=740)  

        # Button
        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkgreen", fg="white", command=self.face_recog)
        b1_1.place(x=410, y=626, width=200, height=40)

    # Face Recognition
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="as.masrafi2.k", database="student_db")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student Id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                if confidence > 77: 
                    cv2.putText(img, f"Name: {n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 3) 
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

            return img

        def recognize(img, clf, faceCascade):
            img = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
        clf = cv2.face.LBPHFaceRecognizer_create() 
        clf.read("classifier.xml")    

        video_cap = cv2.VideoCapture(0)

        # Wait for 10 seconds before starting face recognition
        time.sleep(10)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    obj = Face_Recognition(root)
    root.mainloop()
