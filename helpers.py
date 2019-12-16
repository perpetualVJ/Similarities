from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""

    l1 = a.splitlines()
    l2 = b.splitlines()

    s1 = set(l1)
    s2 = set(l2)

    l = [i for i in s1 if i in s2]

    return l


def sentences(a, b):
    """Return sentences in both a and b"""
    l1 = set(sent_tokenize(a))
    l2 = set(sent_tokenize(b))
    return l1 & l2


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    l1 = []
    for i in range(0,len(a) - n + 1):
        l1.append(a[i:i+n])

    l2 = []
    for i in range(0,len(b) - n + 1):
        l2.append(b[i:i+n])

    s1 = set(l1)
    s2 = set(l2)
    #print(s1)
    #print(s2)
    l = [x for x in s1 if x in s2]
    #print(l)
    return l
