class Data:
    """
    Holds the data extracted from the sensor in addition to functions for manipulating the data, such as graphing,
    averaging, finding mins and maxes.

    TODO:
    Add download function
    Add graphing
    Add averaging, mins, maxes
    Add converstions between Fahrenheit and Celsius
    """

    temps = [] #Holds the temperature at each sample time
    times = [] #Time each sample was taken at (Local time)
    fileType = "txt"

    def setFile(self, ext):
        fileType = ext