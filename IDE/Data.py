import matplotlib.pyplot as plt
import numpy as np


class Data:
    """
    Holds the data extracted from the sensor in addition to functions for manipulating the data, such as graphing,
    averaging, finding mins and maxes.
    Defaults output to txt

    TODO:
    Add download function
    Add graphing
    Add averaging, mins, maxes
    Add converstions between Fahrenheit and Celsius
    """

    temps = [] #Holds the temperature at each sample time
    times = [] #Time each sample was taken at in milliseconds after start(starts at 0)
    startTime = (0,0,0,0,0,0.0) #Holds time data collection started at (Military time) (dd/mm/yyyy/hh/mm/ss)
    fileType = "txt"
    avg = 0.0
    max = 0.0
    min = 0.0
    std = 0.0

    def setFile(self, ext):
        self.fileType = ext

    def graphData(self):
        plt.plot(self.times,self.temps)
        plt.xlabel("Time (ms)")
        plt.ylabel("Temperature (C)")
        plt.show()

    def findStats(self):
        """
        Sets the average, min, and max temperature of the array and the standard deviation of the data
        collected
        """
        data = np.array(self.temps)
        self.avg = np.mean(data)
        self.max = np.amax(data)
        self.min = np.amin(data)
        self.std = np.std(data)

    def downloadData(self):
        """
        This method will download the temperature data from the Ardunio.
        For now this method just creates a random array of floats
        :return:
        """
        self.temps = np.random.rand(100)*100 - 20
        self.times = np.array(range(100))*100
        self.temps.tolist()
        self.times.tolist()

    def printStats(self):
        """
        Used for debugging
        :return:
        """
        print("Avg: " + str(self.avg))
        print("Max: " + str(self.max))
        print("Min: " + str(self.min))
        print("Std: " + str(self.std))


#Debugging
#"""
data = Data()
data.downloadData()
print(data.temps)
print(data.times)
data.graphData()
data.findStats()
data.printStats()
#"""



