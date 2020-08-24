import os

class Resources():
    def __init__(self, basepath):
        self.basepath = os.path.abspath(basepath)
    
    def getpath(self, path):
        return os.path.join(self.basepath, path)