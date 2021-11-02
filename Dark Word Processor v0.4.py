# By Brandon. Started 10/5/2021 11:40 PM.
# Dark Word Processor Version 0.4
# By Brandon Chung
# v0.1 Created: 10/5/2021
# v0.4 Created: 4/10/2021
# Last Updated: 14/10/2021

# Libraries used

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from string import *

# Importing file pointer

from os import path
dir_path=path.dirname(path.realpath(__file__))

def create_main():

    # Initiating tkinter

    main = Tk()


    # Declaring geometry variables

    screen_width, screen_height = main.maxsize()    # Max window size
    main_h = screen_height//2                       # Main window height
    main_w = (main_h//3)*4                          # Main window width

    # Declaring font variables

    std_lbl_w = main_w//3                           # Standard font width
    std_lbl_h = std_lbl_w//10                       # Standard font height
    std_font = ('Verdana',std_lbl_h//2)             # Standard font


    # Defining standard functions

    def std_label(window, string):
        label = ttk.Label(window, text = str(string), background = 'black', foreground = 'white', font = std_font)
        return label

    def std_txt(window, string):
        txt = Text(window, background = 'black', foreground = 'white', insertbackground = 'white', font = std_font, undo = True, autoseparators = True, maxundo = 0, wrap = WORD)
        txt.insert(END,f'{string}')
        return txt


    ## Main Window Config ##

    main.columnconfigure(0, weight = 1)
    main.rowconfigure(0, weight = 1)
    main.config(background = 'black')
    main.title('Dark Word Processor v0.4')
    main.geometry(f'{main_w}x{main_h}')


    ### Text area ###

    txtarea = std_txt(main, '')
    txtarea.grid(sticky = N+E+S+W)


    ### Menu Bar ###

    menubar = Menu(main)

    ## File Menu ##

    filename = ''

    # New #

    def filenew():

        nonlocal filename # Use nonlocal so that the variable stays in the function

        # Reset program
        
        filename = ''
        main.title('Dark Word Processor v0.4')
        txtarea.delete(1.0,END)

    def filesave():

        nonlocal filename # Use nonlocal so that the variable stays in the function


        # Save file

        if filename != '':

            file=open(f'{filename}','w')
            file.write(txtarea.get(1.0,'end-1c'))
            file.close()
            main.title(path.basename(filename) + " - Dark Word Processor v0.4")
            print(path.basename(filename))

        # If no file is selected, go to filesaveas

        else:
            filesaveas()

    def filesaveas():

        nonlocal filename # Use nonlocal so that the variable stays in the function

        # Save file as

        checkfilename = asksaveasfilename(initialfile='Untitled.txt',defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])
        main.lift() # Make sure current window is brought back to the top

        if checkfilename != '':

            filename = checkfilename

            file=open(f'{filename}','w')
            file.write(txtarea.get(1.0,'end-1c'))
            file.close()
            main.title(path.basename(filename) + " - Dark Word Processor v0.4")

        # Ignore if no file is selected

        else:
            pass


    def fileopen():

        nonlocal filename # Use nonlocal so that the variable stays in the function

        # Open file

        checkfilename = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        main.lift() # Make sure current window is brought back to the top

        if checkfilename != '':

            filename = checkfilename

            file = open(filename,'r')

            txtarea.delete(1.0, END)
            txtarea.insert(END,file.read())
            file.close()
            main.title(path.basename(filename) + " - Dark Word Processor v0.4")

        # Ignore if no file is selected

        else:
            pass

    filemenu = Menu(menubar,tearoff=0, background = 'black', foreground = 'white', font = std_font)
    filemenu.add_command(label = 'New', command = lambda: filenew())
    filemenu.add_command(label = 'Save', command = lambda: filesave())
    filemenu.add_command(label = 'Save As', command = lambda: filesaveas())
    filemenu.add_command(label = 'Open', command = lambda: fileopen())
    filemenu.add_command(label = 'Duplicate', command = lambda: create_main()) # Repeats current function to create an isolated word processor
    menubar.add_cascade(label='File',menu=filemenu, font = std_font)

    ## Information ##

    # Word Count #

    def word_count(txtarea):

        # Initialize information window
        word_count_window = Toplevel(main)
        word_count_window.title('Word Count')
        word_count_window.config(background = 'black')
        word_count_window.geometry(f'{std_lbl_w*2}x{std_lbl_h*4}')

        txt = str(txtarea.get(1.0, 'end-1c'))

        # Words #

        words = len(txt.split())
        lbl_words = std_label(word_count_window, f'Word count: {words}')
        lbl_words.grid(column = 0, row = 0, sticky = E)

        # Characters (No Spaces) #

        characters_no_space = len(txt.replace('\n','').replace(' ','')) # Must have two .replace() because both new line and whitespace can not be detected in the same comma
        lbl_characters_no_space = std_label(word_count_window, f'Characters (no space): {characters_no_space}')
        lbl_characters_no_space.grid(column = 0, row = 1, sticky = E)

        # Characters (With Spaces) #

        characters_with_space = len(txt.replace('\n',''))
        lbl_characters_with_space = std_label(word_count_window, f'Characters (with space): {characters_with_space}')
        lbl_characters_with_space.grid(column = 0, row = 2, sticky = E)

        # Lines #

        lines = txt.count('\n') + 1
        lbl_lines = std_label(word_count_window, f'Lines: {lines}')
        lbl_lines.grid(column = 0, row = 3, sticky = E)



    informationmenu = Menu(menubar, tearoff = 0, background = 'black', foreground = 'white', font = std_font)
    informationmenu.add_command(label = 'Word Count', command = lambda: word_count(txtarea))
    menubar.add_cascade(label='Information',menu=informationmenu, font = std_font)

    ### End of Menu Bar ###
    main.config(menu=menubar)

    main.mainloop()

create_main()