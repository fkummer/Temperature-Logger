"""
This file will display the GUI to the user. It will display options to change the rate or duration of data collection
as well as options to extract the data as a csv or text file and create a graph of the data.
TODO:
Create widgets for:
    Setting rate of collection
    Setting duration of collection
    Setting filetype of collected data
    Making graph of the collected data
Make data extractable as a matlab compatable array
"""

import tkinter as tk

def guiInit(window):
    uploadButton = tk.Button(window, text = "Upload settings")
    downloadButton = tk.Button(window, text = "Download data")



root = tk.Tk() #Main window of GUI
root.mainloop()