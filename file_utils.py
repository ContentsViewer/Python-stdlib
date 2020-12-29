import os
import pathlib
from datetime import datetime


def get_unique_log_dir():
    date = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
    pid = os.getpid()
    return pathlib.Path(f'{date}({pid})')