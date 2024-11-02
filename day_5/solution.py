"""
Solution for day 5 task
"""

def cons(a, b):
    """Constructs a pair"""
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    """Returns the first element of the pair"""
    return pair(lambda a, _b: a)

def cdr(pair):
    """Returns the last element of the pair"""
    return pair(lambda _a, b: b)
