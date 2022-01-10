class VanEmdeBoas:
    def __init__(self, size):
        self.size = size
        self.min = None
        self.max = None
        self.sqrootsize = int(self.size ** 0.5)
        if size == 2:
            return
        self.summary = VanEmdeBoas(self.sqrootsize)
        self.clusture = [VanEmdeBoas(self.sqrootsize) for _ in range(self.sqrootsize)]

    def high(self, x):
        return x // self.sqrootsize

    def low(self, x):
        return x % self.sqrootsize

    def index(self, i, j):
        return (i * self.sqrootsize) + j

    def insert(self, x):
        if self.min is None:
            self.min = self.max = x
        if x < self.min:
            x, self.min = self.min, x
        if self.max < x:
            self.max = x
        if self.size <= 2:
            return
        if self.clusture[self.high(x)].min is None:
            self.summary.insert(self.high(x))
        self.clusture[self.high(x)].insert(self.low(x))

    def delete(self, x):
        if self.size <= 2:
            if x == self.min:
                if self.min == self.max:
                    self.min = self.max = None
                else:
                    self.min = self.max
            else:
                self.max = self.min
            return
        if x == self.min:
            i = self.summary.min
            if i is None:
                self.min = self.max = None
                return
            x = self.min = self.index(i, self.clusture[i].min)
        self.clusture[self.high(x)].delete(self.low(x))
        if self.clusture[self.high(x)].min is None:
            self.summary.delete(self.high(x))
        if x == self.max:
            i = self.summary.max
            if i is None:
                self.max = None
            else:
                self.max = self.index(i, self.clusture[i].max)

    def succesor(self, x):
        if self.size <= 2:
            if x < self.min:
                return self.min
            else:
                return self.max
        i = self.high(x)
        if self.low(x) < self.clusture[i].max:
            j = self.clusture[i].succesor(self.low(x))
        else:
            i = self.summary.succesor(i)
            j = self.clusture[i].min
        return self.index(i, j)
