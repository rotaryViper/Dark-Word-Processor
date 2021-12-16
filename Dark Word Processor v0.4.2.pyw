# By Brandon. Started 10/5/2021 11:40 PM.
# Dark Word Processor Version 0.4
# v0.1 Created: 10/5/2021
# v0.4.2 Created: 14/12/2021
# Last Updated: 16/12/2021
# Now with async

# Libraries used

from tkinter import *
from tkinter.filedialog import *
import asyncio

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

    # Declaring Word Process Title
    programTitle = 'Dark Word Processor v0.4.2'

    # Defining standard functions

    def std_label(window, string):
        label = Label(window, text = str(string), background = 'black', foreground = 'white', font = std_font)
        return label

    def std_txt(window, string):
        txt = Text(window, background = 'black', foreground = 'white', insertbackground = 'white', font = std_font, undo = True, autoseparators = True, maxundo = 0, wrap = WORD)
        txt.insert(END,f'{string}')
        return txt


    ## Main Window Config ##

    main.columnconfigure(0, weight = 1)
    main.rowconfigure(0, weight = 1)
    main.config(background = 'black')
    main.title(programTitle)
    main.geometry(f'{main_w}x{main_h}')


    ### Text area ###

    txtarea = std_txt(main, '')
    txtarea.grid(row=0, column = 0, sticky = N+E+S+W)

    ### Menu Bar ###

    menubar = Menu(main)

    ## File Menu ##

    filename = ''

    # New #

    async def filenew():

        nonlocal filename # Use nonlocal so that the variable stays in the function

        # Reset program
        
        filename = ''
        main.title(programTitle)
        txtarea.delete(1.0,END)

    async def filesave():

        nonlocal filename # Use nonlocal so that the variable stays in the function


        # Save file

        if filename != '':

            with open(filename, 'w') as file:
                file.write(txtarea.get(1.0,'end-1c'))

            main.title(path.basename(filename) + " - " + programTitle)
            print(path.basename(filename))

        # If no file is selected, go to filesaveas

        else:
            asyncio.create_task(filesaveas())

    async def filesaveas():

        nonlocal filename # Use nonlocal so that the variable stays in the function

        # Save file as

        checkfilename = asksaveasfilename(initialfile='Untitled.txt',defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])
        main.lift() # Make sure current window is brought back to the top

        if checkfilename != '':

            filename = checkfilename

            with open(filename, 'w') as file:
                file.write(txtarea.get(1.0,'end-1c'))
            
            main.title(path.basename(filename) + " - " + programTitle)

        # Ignore if no file is selected

        else:
            pass


    async def fileopen():

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
            main.title(path.basename(filename) + " - " + programTitle)

        # Ignore if no file is selected

        else:
            pass

    filemenu = Menu(menubar,tearoff=0, background = 'black', foreground = 'white', font = std_font)
    filemenu.add_command(label = 'New', command = lambda:asyncio.run(filenew()))
    filemenu.add_command(label = 'Save', command = lambda:asyncio.run(filesave()))
    filemenu.add_command(label = 'Save As', command = lambda:asyncio.run(filesaveas()))
    filemenu.add_command(label = 'Open', command = lambda:asyncio.run(fileopen()))
    filemenu.add_command(label = 'Duplicate', command = lambda:create_main()) # Repeats current function to create an isolated word processor
    menubar.add_cascade(label='File',menu=filemenu, font = std_font)

    ## Information ##

    # Word Count #

    async def word_count(txtarea):

        # Initialize information window
        word_count_window = Toplevel(main)
        word_count_window.title('Word Count')
        word_count_window.config(background = 'black')
        word_count_window.geometry(f'{round(std_lbl_w*1.5)}x{std_lbl_h*4}')

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
    informationmenu.add_command(label = 'Word Count', command = lambda:asyncio.run(word_count(txtarea)))
    menubar.add_cascade(label='Information',menu=informationmenu, font = std_font)

    ### End of Menu Bar ###
    main.config(menu=menubar)

    ## Scroll Bar ##
    scrollbar = Scrollbar(main) # I tried colouring the scrollbar but it doesn't seem to be displayed in windows 11
    scrollbar.grid(row = 0, column = 1, sticky = N+E+S+W)
    # Let txtarea control the scrollbar
    scrollbar.config(command = txtarea.yview)
    txtarea.config(yscrollcommand = scrollbar.set)

    main.mainloop()

create_main()