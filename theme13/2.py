class Counter:
    def __init__(self, max_value):
        self.current = 1
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_value:
            raise StopIteration

        value = self.current
        self.current += 1

        return value


counter = Counter(max_value=4)

for number in counter:
    print(number)


counter_iter = iter(counter)
#
# while True:
#     try:
#         number = next(counter_iter)
#     except StopIteration:
#         break
#
#     print(number)
#
print(next(counter_iter))
print(next(counter_iter))
print(next(counter_iter))
print(next(counter_iter))
print(next(counter_iter))
