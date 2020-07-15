
class Container:

    def add_var(self, name, val):
        setattr(self, name, val)

    def __str__(self):
        res = ''

        for key, value in self.__dict__.items():
            res += str(key) + '\n'
            res += '    ' + str(value) + '\n'

        return res
