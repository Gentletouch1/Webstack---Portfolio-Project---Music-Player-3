from tkinter import *
from PIL import Image,ImageTk
import os
import time
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
from mutagen.mp3 import MP3
import os
import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.title('Gentletouch Music Player')
root.geometry('485x700+290+10')
root.configure(background='black')
root.resizable(False, False)
mixer.init()

frameCnt =30
frames=[PhotoImage(file='aa1.gif', format = 'gif -index %i' %(i)) for i in range(frameCnt)]
                  
def update(ind):

    frame = frames[ind]
    ind +=1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(40,update,ind)  
label=Label(root)
label.place(x=0,y=0)
root.after(0, update, 0)



def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)

        for song in songs:
            if song.endswith('.mp3'):
                Playlist.insert(END, song)

def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name, ACTIVE)
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

lower_frame = Frame(root, bg = 'grey', width=485, height=180)
lower_frame.place(x=0,y=480)

image_icon = PhotoImage(file='logo G3.png')
root.iconphoto(False, image_icon)

Menu = PhotoImage(file = 'menu.png')
Label(root,image = Menu).place(x=0,y=580,width=485,height=100)

Frame_Music = Frame(root, bd =2, relief = RIDGE)
Frame_Music.place(x=0,y=585,width = 485, height=100)


#class musicplayer:
    
#   def Openfile():
#            global filename
#            filename=filedialog.askopenfilename()
#
#      def __init__(self,Tk):
#        self.root=Tk
#        self.menubar=Menu(self.root)
#        self.root.configure(menu=self.menubar)
#
#        self.submenu=Menu(self.menubar,tearoff=0)
#        self.menubar.add_cascade(label='File',menu=self.submenu)
#
#        self.submenu=Menu(self.menubar,tearoff=0)
#        self.menubar.add_cascade(label='Edit',menu=self.submenu)
#        self.submenu.add_command(label='copy')
#        self.submenu.add_command(label='cut')
#        self.submenu.add_command(label='paste')
#
#        self.submenu=Menu(self.menubar,tearoff=0)
#        self.menubar.add_cascade(label='Help',menu=self.submenu)
#        self.submenu.add_command(label='About',command=About)

#      def About():
#      tkinter.messagebox.showinfo('About Us','Music Player created By Gentletouch')



Buttonplay=PhotoImage(file='play1.png')
Button(root,image=Buttonplay, bg='yellow', bd=0, height=60,width=60, command=PlayMusic).place(x=215,y=487)

ButtonStop=PhotoImage(file='stop1.png')
Button(root, image= ButtonStop, bg='yellow', bd=0,height=60,width=60,command=mixer.music.stop).place(x=130,y=487)

ButtonPause=PhotoImage(file='pause1.png')
Button(root, image= ButtonPause, bg='yellow', bd=0,height=60,width=60,command=mixer.music.pause).place(x=300,y=487)

Volume1 = PhotoImage(file='volume.png')
panel=Label(root,image=Volume1).place(x=20,y=487)

Button(root,text='Browse Music', width=59, height=1, font=('calibri',12,'bold'), fg='black', bg='green', command = AddMusic).place(x=0,y=550)

Scroll = Scrollbar(Frame_Music)
Playlist=Listbox(Frame_Music, width=100, font=('Times new roman',10), bg='blue',fg='grey', selectbackground ='lightblue', cursor='hand2',bd=0, yscrollcommand=Scroll.set)
Scroll.config(command = Playlist.yview)
Scroll.pack(side = RIGHT, fill=Y)
Playlist.pack(side=RIGHT,fill=BOTH)


root.mainloop()
