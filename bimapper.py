
class AlreadyBoundException(Exception):
    """Raised when either x or y has been bound with the other."""

    def __init__(self, *args):
        Exception.__init__(self, 'Already Bound', *args)

# Bijection Mapper
class BiMapper():
    def __init__(self):
        self.x2y = {}
        self.y2x = {}

    def bind(self, x, y):
        """
        Raises
        ------
        AlreadyBoundException:
            Raises AlreadyBoundException if x and y have been already bound.
        """
        
        if x in self.x2y or y in self.y2x:
            raise AlreadyBoundException()
        
        self.x2y[x] = y
        self.y2x[y] = x

    def unbind_x(self, x):
        if not x in self.x2y: return

        y = self.x2y.pop(x)
        self.y2x.pop(y)

    def unbind_y(self, y):
        if not y in self.y2x: return

        x = self.y2x.pop(y)
        self.x2y.pop(x)
