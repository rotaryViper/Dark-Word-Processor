# By Brandon. Started 10/5/2021 11:40 PM.
import os
dir_path=os.path.dirname(os.path.realpath(__file__))

white = '#FFFFFF'
black = '#000000'
grey = '#808080'
green = '#00FF00'
red = '#FF0000'

from tkinter import *
main_gui=Tk()
main_gui.title('Dark Word Processor')
main_gui.geometry('640x480')
main_gui.config(bg=black)

txtsize = 12
txtwidth = 250
txtheight = 25
Verdana='Verdana'

def to_do_list():
        lbl_title=Label(main_gui,text='To Do List')
        lbl_title.configure(background=black,fg=white,font=(Verdana,txtsize))
        lbl_title.place(height=txtheight,width=120,x=10,y=140)

        txt_to_do_list=Text(main_gui)
        txt_to_do_list.configure(background=black,fg=white,font=(Verdana,txtsize),wrap=WORD,insertbackground=white)
        txt_to_do_list.place(height=124,width=125,x=10,y=170)

        content=open(f'{dir_path}\To_do_list.txt')
        content=(content.read())

        txt_to_do_list.insert(END,content)

        def save_list():
                input=txt_to_do_list.get('1.0','end-1c')

                file=open(f'{dir_path}\Test.txt','w')

                file.write(input)
                file.close
                
        btn_save=Button(main_gui,text='Save',command=save_list)
        btn_save.configure(background=black,fg=white,font=(Verdana,txtsize))
        btn_save.place(height=30,width=45,x=134,y=265)

def page():

        txt_title=Text(main_gui)
        txt_title.configure(background=black,fg=white,font=('Roboto',txtsize),insertbackground=white)
        txt_title.place(width=400,height=30,x=70,y=10)

        txt_page=Text(main_gui)
        txt_page.configure(background=black,fg=white,font=('Roboto',txtsize),wrap=WORD,insertbackground=white)
        txt_page.place(width=620,height=430,x=10,y=40)

        try:
                content=open(f'{dir_path}\Test.txt')
                content=(content.read())
                txt_page.insert(END,content)

        except:
                pass

        def save_list():
                input=txt_page.get('1.0','end-1c')

                file=open(f'{dir_path}\{txt_title}.txt','w')

                file.write(input)
                file.close

        btn_save=Button(main_gui,text='Save',command=save_list)

        btn_save.configure(background=black,fg=white,font=('Roboto',txtsize))
        btn_save.place(width=60,height=30,x=10,y=10)

page()
main_gui.mainloop()