from tkinter import *
import tkinter as tk
import os
from tkinter import messagebox
from tkinter import filedialog
import glob
import shutil
import datetime

root = tk.Tk()
root.title('Check files')





# Functions
def GetFileList(path, type):    #Return a list of filename matching the given path and file type
    return glob.glob(path + "*" + type)


def ask_quit():
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # this closes app
        root.destroy()
        

def ask_dir():
    dirname = filedialog.askdirectory()
    for data in dirname:
        txt_frame1.delete(0,END)
        txt_frame1.insert(END,dirname)

def ask_dir2():
    dirname = filedialog.askdirectory()
    for data in dirname:
        txt_frame2.delete(0,END)
        txt_frame2.insert(END,dirname)

def job():
    for file in fileList:
        # Get last modified date and today's date
        modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(file))
        todaysDate = datetime.datetime.today()
                
        # Create a list from the filepath
        filePathList = file.split("\\")
        # The last element is the filename
        filename = filePathList[-1]
                
        # If modified within last 24 hours, then copy to destination folder
        modifyDateLimit = modifyDate + datetime.timedelta(days=1)

        # If the file was edited less then 24 hours ago then copy it
        if modifyDateLimit > todaysDate:
            shutil.copy2(file, destinationPath + filename)

    



# Buttons
button = tk.Button(root, text='Browse...',width=12, command=ask_dir)
button.grid(row=0, column=0, padx=25, pady=15)

button2 = tk.Button(root, text='Browse...',width=12, command=ask_dir2)
button2.grid(row=1, column=0, padx=25)

button3 = tk.Button(root, text='Copy files...',width=12, height=2, command=job)
button3.grid(row=2, column=0, padx=25, pady=15)

button4 = tk.Button(root, text='Close Program',width=12, height=2, command=ask_quit)
button4.grid(row=2, column=1, padx=20, pady=15, sticky=E)



# Text Boxes
txt_frame1 = tk.Entry(root, text='',width=50)
txt_frame1.grid(row=0, column=1, padx=20)

txt_frame2 = tk.Entry(root, text='',width=50)
txt_frame2.grid(row=1, column=1, padx=20)


# Paths to source/destination folders also file type
originPath = "./Origin/"
destinationPath = "./Destination/"
fileType = ".txt"
# Make list of files in origin folder that end in .txt
fileList = GetFileList(originPath, fileType)



root.mainloop()
