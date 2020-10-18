import webbrowser
from tkinter import *
import tkinter as tk
from tkinter import messagebox

# import python_html

root = tk.Tk()
root.title('Write to HTML')





def ask_quit():
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # this closes app
        root.destroy()

def addToSite():
    var_html = txt_frame1.get()

    f = open("demofile2.html", "w")
    f.write("""<html> 
     <body> 
	<h1>""")
    f.write(var_html)
    f.write("""
        </h1>
     </body> 
</html> """)
    f.close()

# Open and read the file after the appending:
    f = open("demofile2.html", "r")
    print(f.read())

    webbrowser.open_new_tab('demofile2.html')

# Buttons
button = tk.Button(root, text='Change to...',width=12, command=addToSite)
button.grid(row=0, column=0, padx=25, pady=15)


button4 = tk.Button(root, text='Close Program',width=12, height=2, command=ask_quit)
button4.grid(row=2, column=1, padx=20, pady=15, sticky=E)



# Text Boxes
txt_frame1 = tk.Entry(root, text='',width=50)
txt_frame1.grid(row=0, column=1, padx=20)

var_html = txt_frame1.get()





root.mainloop()
