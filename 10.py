def sixes (x):
    return either (eq(x, 6), _yield(sixes, x))

####
take(3, call_goal(call_fresh (lambda x: either(fives(x), sixes(x)))))
