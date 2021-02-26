import time


class FixedLoop():
    """
    Manage loop sync with ensuring a constant execution frequency.

    """
    
    interval_secs = 0
    _last_fixed_time = 0

    def __init__(self, interval_secs):
        self.interval_secs = interval_secs

    def reset(self):
        self._last_fixed_time = time.time()

    def sync(self, sleep=True):
        if self._last_fixed_time == 0:
            self._last_fixed_time = time.time()

        next_time = self.next_fixed_time
        delay_time = next_time - time.time()
        self._last_fixed_time = next_time  # Update the prev time ready for the next call

        if delay_time > 0 and sleep:
            time.sleep(delay_time)
        
        return delay_time

    @property
    def last_fixed_time(self):
        return self._last_fixed_time

    @property
    def next_fixed_time(self):
        return self._last_fixed_time + self.interval_secs
