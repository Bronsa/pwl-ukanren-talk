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

####
call_goal(call_fresh (lambda q: eq(q, 23)))
