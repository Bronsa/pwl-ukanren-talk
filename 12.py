# disj+
def any (goals):
    return reduce(either, goals)

# conj+
def all (goals):
    return reduce(both, goals)

# conde
def cond (goals_s):
    return any(map(all,goals_s))

####
take(3, call_goal(call_fresh(lambda x: cond([[fives(x), sixes(x)],
                                             [sixes(x)]]))))
