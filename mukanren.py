# http://webyrd.net/scheme-2013/papers/HemannMuKanren2013.pdf

from functools import reduce

def var (x): return frozenset([x])

def is_var (x): return type(x) is frozenset

def cons (x,y): return (x,y)

def head (x): return None if x is None else x[0]

def tail (x): return None if x is None else x[1]

def is_cons (x): return type(x) is tuple

# unit
def new_stream (state): return cons(state, None)

# walk
def resolve (term, subst_map):
    if is_var(term) and term in subst_map:
        return resolve(subst_map[term], subst_map)
    else:
        return term

def extend (subst_map, key, val):
    subst_map = subst_map.copy()
    subst_map[key] = val
    return subst_map

def unify (term1, term2, subst_map):
    if subst_map is None:
        return None
    term1 = resolve(term1, subst_map)
    term2 = resolve(term2, subst_map)
    if is_var(term1) and is_var(term2) and term1 == term2:
        return subst_map
    elif is_var(term1):
        return extend (subst_map, term1, term2)
    elif is_var(term2):
        return extend(subst_map, term2, term1)
    elif is_cons(term1) and is_cons(term2):
        subst_map = unify(head(term1), head(term2), subst_map)
        return unify(tail(term1), tail(term2), subst_map)
    elif term1 == term2:
        return subst_map

empty_state = ({}, 0)

def call_goal (goal):
    return goal(empty_state)

def eq (term1, term2):
    def lam (state):
        subst_map = unify(term1, term2, state[0])
        if subst_map:
            return new_stream((subst_map, state[1]))
    return lam

def call_fresh (f):
    def lam (state):
        return f(var(state[1])) ([state[0], state[1] + 1])
    return lam

def call_fresh2 (f):
    def lam (state):
        return f(var(state[1]), var(state[1] +1)) ([state[0], state[1] + 2])
    return lam

def call_fresh3 (f):
    def lam (state):
        return f(var(state[1]), var(state[1] + 1), var(state[1] + 2)) ([state[0], state[1] + 3])
    return lam

# mplus
def append (stream1, stream2):
    if stream1 is None:
        return stream2
    elif callable(stream1):
        return lambda: append (stream2, stream1())
    else:
        return cons(head(stream1), append(stream2, tail(stream1)))

# bind
def mappend (goal, stream):
    if stream is None:
        return None
    elif callable(stream):
        return lambda: mappend(goal, stream())
    else:
        return append(goal(head(stream)), mappend(goal, tail(stream)))

# disj
def either (goal1, goal2):
    return lambda state: append(goal1(state), goal2(state))

# conj
def both (goal1, goal2):
    return lambda state: mappend(goal2, goal1(state))

# mplus
def append (stream1, stream2):
    if stream1 is None:
        return stream2
    elif callable(stream1):
        return lambda: append (stream1(), stream2)
    else:
        return cons(head(stream1), append(tail(stream1), stream2))

# zzz
def _yield (f, *args):
    return lambda state: lambda: f(*args) (state)

def pull (stream):
    if callable(stream):
        return pull(stream())
    else:
        return stream

def take (n, stream):
    if n == 0:
        return []
    else:
        stream = pull(stream)
        if stream is None:
            return []
        else:
            ret = [head(stream)]
            ret.extend(take(n-1, tail(stream)))
            return ret

# disj+
def any (goals):
    return reduce(either, goals)

# conj+
def all (goals):
    return reduce(both, goals)

# conde
def cond (goals_s):
    return any(map(all,goals_s))

# appendo
def concat (l, r, out):
    return _yield(call_fresh3,
                  (lambda a, d, res:
                   cond([[eq(None, l),
                          eq(r, out)],

                         [eq(cons(a, d), l),
                          eq(cons(a, res), out),
                          _yield(concat, d, r, res)]])))

# walk*
def deep_resolve (term, subst_map):
    term = resolve(term, subst_map)
    if is_cons(term):
        return cons(deep_resolve(head(term),subst_map),
                    deep_resolve(tail(term),subst_map))
    else:
        return term

def reify (state):
    return deep_resolve(var(0), state[0])

def run (n, f):
    return list(map(reify, take(n, call_goal(call_fresh(f)))))
