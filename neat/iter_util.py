class _PicklableCount:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self._current = start

    def __iter__(self):
        return self

    def __next__(self):
        result = self._current
        self._current += self.step
        return result

    def __getstate__(self):
        return (self._current, self.step)

    def __setstate__(self, state):
        self._current, self.step = state

def count(start=0, step=1):
    """A picklable version of itertools.count()."""
    return _PicklableCount(start, step)