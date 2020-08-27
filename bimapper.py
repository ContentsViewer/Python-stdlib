
class AlreadyLinkedException(Exception):
    """Raised when either x or y has been linked with the other."""

    def __init__(self, *args):
        Exception.__init__(self, 'Already Linked', *args)

# Bijection Mapper
class BiMapper():
    def __init__(self):
        self.x2y = {}
        self.y2x = {}

    def link(self, x, y):
        if x in self.x2y or y in self.y2x:
            raise AlreadyLinkedException()
        
        self.x2y[x] = y
        self.y2x[y] = x

    def unlink_x(self, x):
        if not x in self.x2y: return

        y = self.x2y.pop(x)
        self.y2x.pop(y)

    def unlink_y(self, y):
        if not y in self.y2x: return

        x = self.y2x.pop(y)
        self.x2y.pop(x)
