import time


class FixedLoop():
    interval = 0
    _last_fixed_time = 0
    _last_delay_time = 0

    def __init__(self, interval):
        self.interval = interval

    def reset(self):
        self._last_fixed_time = time.time()

    def sync(self):
        if self._last_fixed_time == 0:
            self._last_fixed_time = time.time()

        next_time = self.next_fixed_time
        delay_time = next_time - time.time()
        self._last_fixed_time = next_time  # Update the prev time ready for the next call
        self._last_delay_time = delay_time

        if delay_time > 0:
            time.sleep(delay_time)
            return True

        if delay_time == 0:
            # return Immediately
            return True

        if delay_time < 0:
            return False

    @property
    def last_delay_time(self):
        return self._last_delay_time

    @property
    def last_fixed_time(self):
        return self._last_fixed_time

    @property
    def next_fixed_time(self):
        return self._last_fixed_time + self.interval
