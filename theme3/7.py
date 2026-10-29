# from numpy import array
#
# arr = array(["Python", "Java", "C++", "Python"])

languages = ["Python", "Java", "C++", "Python"]
print(len(languages))
print(languages[0])
print(languages[1])
print(languages[2])

languages[1] = "JavaScript"

print(languages)

languages.append("Rust")
print(languages)

languages.remove("Python")
print(languages)

languages.append(123)
print(languages)

languages.append(988.111)
print(languages)

languages.extend([98, 99, 100])
print(languages)


print("Python" in languages)