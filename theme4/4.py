words_first = ["яблоко", "банан"]
words_second = words_first

print(words_first)
print(words_second)

words_copy1 = words_first.copy()
words_copy2 = words_first[:]

words_first.append("арбуз")

print(words_first)
print(words_second)

print(words_copy1)
print(words_copy2)