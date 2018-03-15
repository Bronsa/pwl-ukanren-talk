# walk
def resolve (term, subst_map):
    if is_var(term) and term in subst_map:
        return resolve(subst_map[term], subst_map)
    else:
        return term

####
resolve (var (1), {var(1): var(2), var(2): 3})
