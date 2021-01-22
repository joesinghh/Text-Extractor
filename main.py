from tkinter import *
from tkinter.messagebox import showwarning,showerror
from tkinter.filedialog import askopenfile
import cv2
from PIL import Image, ImageTk
from threading import Thread
from tesseract import ProcessImage

#display result
def extractimg(img): 
    result = Toplevel(mainframe)
    result.title('Result')
    result.geometry('300x300')
    text = Text(result,wrap=WORD)
    text.place(relwidth=1,relheight=1)
    text.insert(END,ProcessImage(img))

#camera Cature display
def display():

    rep,frame = cap.read()
    frame = cv2.flip(frame,1)
    cv2img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    img = Image.fromarray(cv2img)
    imgtk = ImageTk.PhotoImage(image=img)
    screen.imgtk = imgtk
    screen.configure(image=imgtk)
    if val==0:
        camera.destroy()
        cap.release()
        img = img.convert('RGB')
        img = img.save("test.jpg","JPEG",quality=80, optimize=True, progressive=True)
        extractimg('test.jpg')
        
    else:
        camera.after(10,display)

#select image and extract text
def open_img():
    path = askopenfile(title="Select Image",filetypes=[("Jpg",".jpg"),("Png",".png")])
    if path!=None:
        extractimg(path.name)

#stop camera display
def snap_():
    global val
    val=0

#open camera window
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
    cap = cv2.VideoCapture(0) #Video capture object ( 0 - default camera , 1 - second camera , and so on)
    display()

#main window
root = Tk()
#size of window
root.geometry('600x600'); 
root.title("Text Extractor");

#Frames
startframe = Frame(root)
mainframe = Frame(root)
saveas = Frame(root)
startframe.place(relheight=1,relwidth=1)
mainframe.place(relheight=1,relwidth=1)
saveas.place(relheight=1,relwidth=1)

startframe.tkraise()

#Mainframe
opencam = Button(mainframe,text='Open Cam',command=opencam)
opencam.place(relheight=0.1,relwidth=0.3,relx=0.2,rely=0.2)

selectimg = Button(mainframe,text='Select Image',command = open_img);
selectimg.place(relheight=0.1,relwidth=0.3,relx=0.5,rely=0.2)

#start Frame
Start = Button(startframe,text='start',command= mainframe.tkraise)
Start.place(relheight=0.15,relwidth=0.3,relx=0.4,rely=0.4)

root.mainloop()