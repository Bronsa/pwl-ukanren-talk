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

####
run (1, lambda q: concat(cons(1, None),
                         cons(2, None),
                         q))
run (1, lambda q: concat(cons(1, None),
                         q,
                         cons(1, cons(2, None))))
run (3, lambda q: call_fresh2(lambda a, b: all([concat(a, b, cons(1, cons(2, None))),
                                                eq(cons(a, b), q)])))
