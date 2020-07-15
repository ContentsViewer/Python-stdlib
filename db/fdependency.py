
class FDependency:
    """
    Function dependecy class

    Example:
    fd1 = FDependency(['A','B'],['C'])
    fd2 = FDependency(['B'],['D'])
    fd3 = FDependency(['A','B','E'],['C','D'])
    fd4 = FDependency(['C','D'],['E'])
    fd5 = FDependency(['C','E'],['A'])
    """

    def __init__(self, lh, rh):
        self.lh = lh
        self.rh = rh

    def __str__(self):
        return str(self.lh) + ' -> ' + str(self.rh)

    def __eq__(self, other):
        return set(self.lh) == set(other.lh) and set(self.rh) == set(other.rh)
