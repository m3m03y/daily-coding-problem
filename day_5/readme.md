# Day 5

#medium #jane_street

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:
```
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```
Implement car and cdr.

## Resources:
- https://www.learnpython.org/en/Closures
- https://dev.to/blugreenspace/understanding-closures-in-python-bbl