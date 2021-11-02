# By Brandon. Started 10/5/2021 11:40 PM.
# Dark Word Processor Version 0.2
# Created: 10/5/2021
# Last Updated: 17/5/2021
import os
dir_path=os.path.dirname(os.path.realpath(__file__))

white='#FFFFFF'
black='#000000'
grey='#808080'
green='#00FF00'
red='#FF0000'

from tkinter import *
from tkinter.filedialog import *
main=Tk()
main.title('Dark Word Processor')
main.geometry('640x480')

txtsize=12
txtwidth=250
txtheight=25

menubar=Menu(main,bg=black,fg=white,font=('Verdana',txtsize))
txtarea=Text(main,bg=black,fg=white,font=('Verdana',txtsize),wrap=WORD,insertbackground=white)
filemenu=Menu(menubar,tearoff=0,bg=black,fg=white)
editmenu=Menu(menubar,tearoff=0)
helpmenu=Menu(menubar,tearoff=0)

fileName=None

main.grid_rowconfigure(0,weight=1)
main.grid_columnconfigure(0,weight=1)

txtarea.grid(sticky=N+E+S+W)

def newFile():
    global fileName
    main.title('Dark Word Processor')
    fileName=None
    txtarea.delete(1.0,'end-1c')

def saveFile():
        global fileName
        if fileName==None:
                fileName=asksaveasfilename(initialfile='Untitled.txt',defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])
                if fileName=='':
                        fileName=None
                else:
                        file=open(f'{fileName}','w')
                        file.write(txtarea.get(1.0,END))
                        file.close()
                        main.title(os.path.basename(fileName) + " - Dark Word Processor")

        else:
                file=open(f'{fileName}','w')
                file.write(txtarea.get(1.0,'end-1c'))
                file.close()

def openFile():
        global fileName
        if fileName=='':
                fileName=None
        else:
                fileName = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
                try:
                    file=open(fileName,'r')
                    txtarea.delete(1.0,END)
                    
                    txtarea.insert(END,file.read())
                    file.close()
                    main.title(os.path.basename(fileName) + " - Dark Word Processor")
                except:
                    pass

filemenu.add_command(label='New',command=newFile)
filemenu.add_command(label='Save',command=saveFile)
filemenu.add_command(label='Open',command=openFile)

menubar.add_cascade(label="File",menu=filemenu)



main.config(menu=menubar)

main.mainloop()
