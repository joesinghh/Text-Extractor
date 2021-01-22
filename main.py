from tkinter import *
from tkinter.filedialog import askopenfile
import cv2
from PIL import Image, ImageTk
from threading import Thread
def save_img(img):
    pass

def display():
    rep,frame = cap.read()
    print(val)
    frame = cv2.flip(frame,1)
    cv2img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2img)
    imgtk = ImageTk.PhotoImage(image=img)
    screen.imgtk = imgtk
    screen.configure(image=imgtk)
    if val==0:
        save_img(cv2img)
        camera.destroy()
        return 0
    else:
        camera.after(10,display)

def open_img():
    path = askopenfile()

def snap_():
    global val
    val=0
def opencam():
    global val,screen,cap,camera
    camera = Toplevel(mainframe)
    camera.title("camera")
    camera.geometry('500x500')
    val = 1
    snap = Button(camera,text='Snap',command = Thread(target=snap_,args=()).start,bg='red')
    snap.place(relheight=0.1,relwidth=0.5,relx=0.4,rely=0.9)
    screen = Label(camera)
    screen.place(relheight=0.90,relwidth=1)
    cap = cv2.VideoCapture(0)
    display()


root = Tk()
root.geometry('600x600');
root.title("Application");
startframe = Frame(root)
mainframe = Frame(root)
startframe.place(relheight=1,relwidth=1)
mainframe.place(relheight=1,relwidth=1)

startframe.tkraise()

opencam = Button(mainframe,text='Open Cam',command=opencam)
opencam.place(relheight=0.1,relwidth=0.3,relx=0.2,rely=0.2)

selectimg = Button(mainframe,text='Select Image',command = open_img);
selectimg.place(relheight=0.1,relwidth=0.3,relx=0.5,rely=0.2)

Start = Button(startframe,text='start',command= mainframe.tkraise)
Start.place(relheight=0.15,relwidth=0.3,relx=0.4,rely=0.4)
root.mainloop()
