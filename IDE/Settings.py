class Settings:
    """
    This class contains the settings for the sensor set by the GUI and functions to upload the settings.

    TODO: Add upload function
    """
    memSize = 10000 #Total number of samples held by sensor
    sampleTime = 100 #Time in milliseconds between samples

    def duration(self, dur):
        """Finds the sample time from a duration"""
        self.sampleTime = int(dur/self.memSize)

    def rate(self, r):
        """Finds the sample time from rate in samples/second"""
        self.sampleTime = int(1000/r)

    def upload(self):
        """Uploads settings to the sensor"""
