# mplus
def append (stream1, stream2):
    if stream1 is None:
        return stream2
    else:
        return cons(head(stream1), append(tail(stream1), stream2))

# bind
def mappend (goal, stream):
    if stream is None:
        return None
    else:
        return append(goal(head(stream)), mappend(goal, tail(stream)))

# disj
def either (goal1, goal2):
    return lambda state: append(goal1(state), goal2(state))

# conj
def both (goal1, goal2):
    return lambda state: mappend(goal2, goal1(state))

####
call_goal(call_fresh (lambda q: either(eq(q, 23), eq(q, 42))))
call_goal(call_fresh (lambda q: both(eq(q, 23), eq(q, 42))))
call_goal(call_fresh (lambda q: both(eq(q, 23), eq(q, 23))))
