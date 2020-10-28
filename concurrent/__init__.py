
class ExitStatus():
    def __init__(self):
        self._result = None
        self._exception = None
    
    def result(self):
        if self._exception is not None:
            raise self._exception

        return self._result

    def exception(self):
        return self._exception

    def set_result(self, result):
        self._result = result

    def set_exception(self, exception):
        self._exception = exception
