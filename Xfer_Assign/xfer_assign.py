import shutil
import os
import glob
import datetime
import time as time_module


# Functions
def GetFileList(path, type):    #Return a list of filename matching the given path and file type
    return glob.glob(path + "*" + type)



# Paths to source/destination folders also file type
originPath = "C:/Projects/Boot_Camp/AdvPython/Xfer_Assign/Folder_A/"
destinationPath = "C:/Projects/Boot_Camp/AdvPython/Xfer_Assign/Folder_B/"
fileType = ".txt"
# Make list of files in origin folder that end in .txt
fileList = GetFileList(originPath, fileType)


#def job():
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

        

