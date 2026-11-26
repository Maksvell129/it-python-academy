class ReverseStepIterator:
    def __init__(self, posled, step):
        self.posled = posled
        self.step = step
        self.index = len(posled) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.posled[self.index]
        self.index -= self.step
        return value


class ReverseStep:
    def __init__(self, posled, step):
        self.posled = posled
        self.step = step

    def __iter__(self):
        return ReverseStepIterator(self.posled, self.step)



class ReverseStep2:
    def __init__(self, posled, step):
        self.posled = posled
        self.step = step

    def __iter__(self):

        for i in range(len(self.posled) - 1, -1, -self.step):
            yield self.posled[i]


test = ReverseStep([1, 2, 3, 4], 1)

print(list(test))

for item in test:
    print(item)



test = ReverseStep([1, 2, 3, 4, 5, 6], 2)

print(list(test))

for item in test:
    print(item)