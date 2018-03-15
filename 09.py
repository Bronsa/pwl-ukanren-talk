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

####
take(3, call_goal(call_fresh (lambda x: fives(x))))
