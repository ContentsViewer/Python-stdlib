import threading
from . import ExitStatus

class SingleThreadExecutor():
    def __init__(self):
        self._is_running = False
    
    def run(self, func, args=(), kwargs={}, done_callback=None):
        if self._is_running:
            return False
        
        def worker():
            exit_status = ExitStatus()

            try:
                result = func(*args, **kwargs)

            except BaseException as exc:
                exit_status.set_exception(exc)
                
            else:
                exit_status.set_result(result)
            
            if done_callback is not None:
                done_callback(exit_status)
            
            self._is_running = False

        self._is_running = True
        thread = threading.Thread(target=worker, daemon=True)
        thread.start()
        
        return True

    @property
    def is_running(self):
        return self._is_running


def run_once_async(func, args=(), kwargs={}, done_callback=None):
    executor = SingleThreadExecutor()
    return executor.run(func, args, kwargs, done_callback)