# appendo
def concat (l, r, out):
    return _yield(call_fresh3,
                  (lambda a, d, res:
                   cond([[eq(None, l),
                          eq(r, out)],

                         [eq(cons(a, d), l),
                          eq(cons(a, res), out),
                          _yield(concat, d, r, res)]])))

####
take(1, call_goal(call_fresh(lambda q: concat(cons(1, None),
                                              cons(2, None),
                                              q))))
