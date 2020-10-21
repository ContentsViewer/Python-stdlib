import threading

class ThreadWorker():
    def __init__(self):
        self.is_running = False
    
    def run(self, func, args=(), kwargs={}, on_finished=None):
        if self.is_running:
            return False
        
        def worker():
            ret = func(*args, **kwargs)

            if on_finished is not None:
                on_finished(ret)

            self.is_running = False

        self.is_running = True
        thread = threading.Thread(target=worker, daemon=True)
        thread.start()
