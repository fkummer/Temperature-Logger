"""
This file will display the GUI to the user. It will display options to change the rate or duration of data collection
as well as options to extract the data as a csv or text file and create a graph of the data.
Ideas:
    Make data extractable as a matlab compatable array
    Be able to select a start time

TODO:
    Create widgets for:
        Setting rate of collection
        Setting duration of collection
        Setting filetype of collected data
        Making graph of the collected data
    Buttons:
        Upload
        Download
    Entries:
        Entry rate
        Entry duration
        (File extension?)
    Checkboxes
        Type of file (txt or csv)
        Graphs
        Min/Max/Average (Could be included on graph)

    Change how GUI handles different filetypes. Current method is messy and makes it difficult to add new filetypes.

"""

import tkinter as tk
import Data
import Settings

class SensorGui(tk.Frame):
    sensorData = Data.Data()
    sensorSettings = Settings.Settings()
    fileType = "txt"

    def __init__(self, parent):
        """Intialize all elements of the GUI"""
        tk.Frame.__init__(self, parent)
        self.uploadButton = tk.Button(self, text = "Upload settings", command=self.uploadSettings)
        self.downloadButton = tk.Button(self, text = "Download data", command=self.downloadData)

        setTxt = lambda: self.setFile("txt")
        setCsv = lambda: self.setFile("csv")
        self.txtFile = tk.Checkbutton(self, text="txt", command=setTxt)
        self.txtFile.select() #Select txt as default
        self.csvFile = tk.Checkbutton(self, text="csv", command=setCsv)

        self.rateSelect = tk.Spinbox(self, from_=1, to=1000)

        self.txtFile.pack(anchor="ne")
        self.csvFile.pack(anchor="ne")
        self.rateSelect.pack(anchor="nw")
        self.uploadButton.pack(anchor="sw")
        self.downloadButton.pack(anchor="se")

    def setFile(self,type):
        """Sets the type of file to be downloaded"""
        if (self.fileType != type):
            print("Filetype switched to " + type)
            self.fileType = type
        else:
            if(type == "txt"):
                print("Filetype switched to csv")
                self.fileType = "csv"
            elif(type == "csv"):
                print("Filetype switched to txt")
                self.fileType = "txt"
        if(type == "txt"):
            self.csvFile.toggle()
        elif(type == "csv"):
            self.txtFile.toggle()


    def uploadSettings(self):
        """Uploads new settings to ardunio"""
        print("Uploading settings...")

    def downloadData(self):
        """Downloads data from the sensor"""
        print("Downloading data...")

root = tk.Tk() #Main window of GUI
root.title("Temperature Sensor IDE")
root.geometry("500x500")
SensorGui(root).pack()
root.mainloop()
