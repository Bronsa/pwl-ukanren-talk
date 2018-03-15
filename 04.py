empty_state = ({}, 0)

# unit
def new_stream (state): return cons(state, None)

def call_goal (goal):
    return goal(empty_state)

def eq (term1, term2):
    def lam (state):
        subst_map = unify(term1, term2, state[0])
        if subst_map:
            return new_stream((subst_map, state[1]))
    return lam

####
call_goal (eq (var(1), 1))
