from .thread_worker import ThreadWorker

class ExitStatus():
    def __init__(self):
        pass

    def result():
        pass

    def exceptino():
        pass

def run_once_async(func, args=(), kwargs={}, on_finished=None):
    worker = ThreadWorker()
    return worker.run(func, args, kwargs, on_finished)