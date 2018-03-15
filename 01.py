from functools import reduce

def var (x): return frozenset([x])

def is_var (x): return type(x) is frozenset

def cons (x,y): return (x,y)

def head (x): return None if x is None else x[0]

def tail (x): return None if x is None else x[1]

def is_cons (x): return type(x) is tuple

def extend (m, key, val):
    m = m.copy()
    m[key] = val
    return m
