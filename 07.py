def fives (x):
    return either (eq(x, 5), fives(x))

####
call_goal(call_fresh (lambda x: fives(x)))
