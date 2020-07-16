"""
based on https://github.com/astagi/lauda

"""
import time
from functools import wraps, partial
from contextlib import contextmanager


class Stopwatch():
    _start_time = 0
    _stop_time = 0
    _checkpoint_time = 0
    _is_running = False

    def start(self):
        if self._is_running:
            return
        self._start_time = time.time()
        self._is_running = True
        self._checkpoint_time = self._start_time
        return

    def stop(self):
        if not self._is_running:
            return
        self._stop_time = time.time()
        self._is_running = False
        return

    def reset(self):
        self.stop()
        self._start_time = 0
        self._stop_time = 0
        self._checkpoint_time = 0
        return

    def restart(self):
        self.reset()
        self.start()
        return

    def checkpoint(self):
        current_time = self._current_time
        self._checkpoint_time, diff_checkpoint = current_time, (
            current_time - self._checkpoint_time)
        return diff_checkpoint

    @property
    def is_running(self):
        return self._is_running

    @property
    def elapsed(self):
        return (self._current_time - self._start_time)

    @property
    def _current_time(self):
        current_time = self._stop_time
        if self.is_running:
            current_time = time.time()
        return current_time


def stopwatch(func=None, callback=None):
    """
    Examples
    --------

        def my_callback(stopwatch, func):
            print(stopwatch.elapsed)

        @stopwatch
        def test():
            time.sleep(1)

        @stopwatch(callback=my_callback)
        def test_with_callback():
            time.sleep(1)

        test()
        test_with_callback()

    """
    if func is None:
        return partial(stopwatch, callback=callback)

    @wraps(func)
    def wrapper(*args, **kwargs):
        stopwatch = Stopwatch()
        stopwatch.start()
        ret = func(*args, **kwargs)
        stopwatch.stop()
        if callback:
            callback(stopwatch, func)
        else:
            print('Executed {0} in {1} seconds'.format(
                func, stopwatch.elapsed))
        return ret
    return wrapper


@contextmanager
def stopwatch_scope(callback=None):
    """
    Examples
    --------

        def my_callback(stopwatch, func):
            print(stopwatch.elapsed)

        def test():
            time.sleep(1)

        with stopwatch_scope():
            test()

        with stopwatch_scope(callback=my_callback):
            test()

    """
    stopwatch = Stopwatch()
    stopwatch.start()
    yield
    stopwatch.stop()
    if callback:
        callback(stopwatch)
    else:
        print('Executed in {0} seconds'.format(stopwatch.elapsed))
