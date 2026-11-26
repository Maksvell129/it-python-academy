
class ListIterator:
    def __init__(self, llist: list):
        self._list = llist
        self._index = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self._index >= len(self._list):
            raise StopIteration

        value = self._list[self._index]
        self._index += 1

        return value



alphabet = ["a", "b", "c"]

for letter in alphabet:
    print(letter)

iter = ListIterator(alphabet)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))