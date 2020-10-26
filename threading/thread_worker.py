import threading

class ThreadWorker():
    def __init__(self):
        self._is_running = False
    
    def run(self, func, args=(), kwargs={}, on_finished=None):
        if self._is_running:
            return False
        
        def worker():
            ret = func(*args, **kwargs)

            if on_finished is not None:
                on_finished(ret)

            self._is_running = False

        self._is_running = True
        thread = threading.Thread(target=worker, daemon=True)
        thread.start()
        
        return True

    @property
    def is_running(self):
        return self._is_running