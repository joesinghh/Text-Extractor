from tkinter import *
from tkinter.messagebox import showwarning,showerror
from tkinter.filedialog import askopenfile
import cv2
from PIL import Image, ImageTk
from threading import Thread
from tesseract import ProcessImage


def stop_():
    camera.destroy()
    cap.release()

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
    snap = Button(camera,text='Snap',command = Thread(target=snap_,args=()).start,bg='#41abf2')
    snap.place(relheight=0.1,relwidth=0.5,relx=0.5,rely=0.9)
    stop = Button(camera,text="Stop",command = stop_,bg='#f50c46',activebackground='#f2417f')
    stop.place(relheight=0.1,relwidth=0.5,relx=0.0,rely=0.9)
    screen = Label(camera)
    screen.place(relheight=0.90,relwidth=1)
    cap = cv2.VideoCapture(0) #Video capture object ( 0 - default camera , 1 - second camera , and so on)
    display()

#main window
root = Tk()
#size of window
root.geometry('600x600'); 
root.title("Text Extractor");
icon = PhotoImage(file='icon.png')
root.iconphoto(True,icon)

#Frames
startframe = Frame(root,bg='#34cceb')
mainframe = Frame(root,bg='#348feb')

startframe.place(relheight=1,relwidth=1)
mainframe.place(relheight=1,relwidth=1)


startframe.tkraise()

#Mainframe
opencam = Button(mainframe,text='Open Cam',command=opencam,bg='#37e6e6',activebackground='#3777e6',fg='black',activeforeground='#37e6e6')
opencam.place(relheight=0.1,relwidth=0.3,relx=0.15,rely=0.3)

selectimg = Button(mainframe,text='Select Image',command = open_img,bg='#37e6e6',activebackground='#3777e6',fg='black',activeforeground='#37e6e6');
selectimg.place(relheight=0.1,relwidth=0.3,relx=0.53,rely=0.3)

#start Frame
Start = Button(startframe,text='Start',command= mainframe.tkraise,bg='#3777e6',fg='#000000',font=('Arial',25,'bold'))
Start.place(relheight=0.15,relwidth=0.3,relx=0.35,rely=0.4)

root.mainloop()