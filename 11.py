# mplus
def append (stream1, stream2):
    if stream1 is None:
        return stream2
    elif callable(stream1):
        return lambda: append (stream2, stream1())
    else:
        return cons(head(stream1), append(tail(stream1), stream2))

####
take(3, call_goal(call_fresh (lambda x: either(fives(x), sixes(x)))))
