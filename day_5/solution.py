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
    def helper(a = None, _b = None):
        return a
    return pair(helper)

def cdr(pair):
    """Returns the last element of the pair"""
    def helper(_a = None, b = None):
        return b
    return pair(helper)
