string = "abc abc abc abc"


def reverse_0(string):
    return " ".join(word[::-1] for word in string.split())


print(reverse_0(string))
