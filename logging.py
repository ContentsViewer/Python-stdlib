import sys
import os
import pathlib
from datetime import datetime


def get_unique_log_dir():
    date = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
    pid = os.getpid()
    return pathlib.Path(f'{date}({pid})')

class TeeLogger(object):
    def __init__(self, file_path):
        self.terminal = sys.stdout
        self.log = file_path.open('a')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass    
