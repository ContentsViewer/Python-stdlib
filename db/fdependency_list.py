from .fdependency import FDependency
from itertools import combinations


class FDependencyList(list):
    """
    Functional dependency list class

    Example:
    fd1 = FDependency(['A','B'],['C'])
    fd2 = FDependency(['B'],['D'])
    fd3 = FDependency(['A','B','E'],['C','D'])
    fd4 = FDependency(['C','D'],['E'])
    fd5 = FDependency(['C','E'],['A'])

    fds = FDependencyList([fd1, fd2, fd3, fd4, fd5])
    """

    def __str__(self):
        string = ''
        for i in range(self.__len__()):
            if i == 0:
                string = string + self[i].__str__()
            else:
                string = string + ', ' + self[i].__str__()
        return string

    def get_lhs(self):
        attr = set()
        for fd in self:
            attr = attr.union(set(fd.lh))
        return list(attr)

    def get_rhs(self):
        attr = set()
        for fd in self:
            attr = attr.union(set(fd.rh))
        return list(attr)

    def attribute_closure(self, attributes):
        """
        Computes the attribute closure with respect to the functional dependencies in the list
        :param attributes: list of attributes for which the closure is to be computed
        :return: list containing the attributes closure
        """

        unused = self[:]  # Copies the self(list)
        # Stores the attribute closure. Is set because no repeated attributes allowed.
        closure = set(attributes)
        closure_len = 0  # Used as stopping condition

        # until no change of closure list
        while closure.__len__() != closure_len:
            closure_len = closure.__len__()
            unused_t = unused[:]
            for fd in unused:
                if set(fd.lh).issubset(closure):
                    unused_t.remove(fd)
                    closure = closure.union(set(fd.rh))
            unused = unused_t[:]
        return list(closure)

    def minimal_cover(self):
        if self == []:
            return []

        return self.make_right_singleton().remove_extraneous().remove_duplicacy()

    def make_right_singleton(self):
        singletons = []
        for fd in self:
            lhs = fd.lh
            rhs = fd.rh
            if len(rhs) > 1:
                for attr in rhs:
                    singletons.append(FDependency(lhs, [attr]))
            else:
                singletons.append(FDependency(fd.lh, fd.rh))
        return FDependencyList(singletons)

    def remove_extraneous(self):
        extraneous_list = []
        ex_flag = 0
        for fd in self:
            lhs = fd.lh
            rhs = fd.rh
            if len(lhs) > 1:
                l = [list(j) for i in range(len(lhs))
                     for j in list(combinations(set(lhs), i + 1))]

                for attr in l:
                    if self.compute_closure_ncheck(attr, rhs):
                        extraneous_list.append(FDependency(attr, rhs))
                        ex_flag = 1
                        break
                    else:
                        ex_flag = 0
                if ex_flag == 0:
                    extraneous_list.append(FDependency(lhs, rhs))
            else:
                extraneous_list.append(FDependency(lhs, rhs))
        return FDependencyList(extraneous_list)

    def remove_duplicacy(self):
        i = 0
        while i < len(self):
            fd = self[i]
            lhs = fd.lh
            rhs = fd.rh
            temp = self.copy()
            temp.remove(fd)
            if FDependencyList(temp).compute_closure_ncheck(lhs, rhs) == 1:
                self.remove(fd)
                continue
            else:
                i = i + 1
        return self

    def compute_closure_ncheck(self, attr, rhs):
        def contains(closure_list, rhs):
            if closure_list.count(rhs[0]) >= 1:
                return 1
            else:
                return 0
        # print(attr, self.attribute_closure(attr))
        if (contains(self.attribute_closure(attr), rhs)) == 1:
            return 1
        else:
            return 0
