from tkinter import *
from tkinter.messagebox import showwarning,showerror
from tkinter.filedialog import askopenfile
import cv2
from PIL import Image, ImageTk
from threading import Thread
from tesseract import ProcessImage

IMAGE = {}

def extractimg(img):
    
    result = Toplevel(mainframe)
    result.geometry('300x300')
    Label(result,text=ProcessImage(img),wrap=True).place(relwidth=1,relheight=1)


def display():

    rep,frame = cap.read()
    frame = cv2.flip(frame,1)
    cv2img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2img)
    imgtk = ImageTk.PhotoImage(image=img)
    screen.imgtk = imgtk
    screen.configure(image=imgtk)
    if val==0:
        camera.destroy()
        cap.release()
        extractimg(cv2img)
        
        
        
    else:
        camera.after(10,display)

def open_img():
    path = askopenfile(title="Select Image",filetypes=[("Jpg",".jpg"),("Png",".png")])
    if path!=None:
        img = Image.open(path)
        save_img(img)

def snap_():
    global val
    val=0
def opencam():
    global val ,screen,cap,camera
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
#Frames
startframe = Frame(root)
mainframe = Frame(root)
saveas = Frame(root)
startframe.place(relheight=1,relwidth=1)
mainframe.place(relheight=1,relwidth=1)
saveas.place(relheight=1,relwidth=1)

startframe.tkraise()

opencam = Button(mainframe,text='Open Cam',command=opencam)
opencam.place(relheight=0.1,relwidth=0.3,relx=0.2,rely=0.2)

selectimg = Button(mainframe,text='Select Image',command = open_img);
selectimg.place(relheight=0.1,relwidth=0.3,relx=0.5,rely=0.2)

extract = Button(mainframe,text='Extract',command=extractimg)
extract.place(relwidth=0.4,relheight=0.1,relx=0.25,rely=0.5)

Start = Button(startframe,text='start',command= mainframe.tkraise)
Start.place(relheight=0.15,relwidth=0.3,relx=0.4,rely=0.4)

root.mainloop()
