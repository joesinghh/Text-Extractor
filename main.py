from tkinter import *
from tkinter.filedialog import askopenfile

def open_img():
    path = askopenfile()
    
root = Tk()
root.geometry('600x600');
root.title("Application");
startframe = Frame(root)
mainframe = Frame(root)
startframe.place(relheight=1,relwidth=1)
mainframe.place(relheight=1,relwidth=1)

startframe.tkraise()

opencam = Button(mainframe,text='Open Cam')
opencam.place(relheight=0.1,relwidth=0.3,relx=0.2,rely=0.2)

selectimg = Button(mainframe,text='Select Image',command = open_img);
selectimg.place(relheight=0.1,relwidth=0.3,relx=0.5,rely=0.2)

Start = Button(startframe,text='start',command= mainframe.tkraise)
Start.place(relheight=0.15,relwidth=0.3,relx=0.4,rely=0.4)
root.mainloop()
