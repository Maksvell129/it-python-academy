from collections import Counter


text = input("Введите текст ")
words = text.split()
print(words)

counted_words = Counter(words)
print(counted_words.most_common()[0][0])

