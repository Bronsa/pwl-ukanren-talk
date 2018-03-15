# mplus
def append (stream1, stream2):
    if stream1 is None:
        return stream2
    elif callable(stream1):
        return lambda: append (stream1(), stream2)
    else:
        return cons(head(stream1), append(tail(stream1), stream2))

# bind
def mappend (goal, stream):
    if stream is None:
        return None
    elif callable(stream):
        return lambda: mappend(goal, stream())
    else:
        return append(goal(head(stream)), mappend(goal, tail(stream)))

# zzz
def _yield (f, *args):
    return lambda state: lambda: f(*args) (state)

def fives (x):
    return either (eq(x, 5), _yield(fives, x))

####
call_goal(call_fresh (lambda x: fives(x)))
