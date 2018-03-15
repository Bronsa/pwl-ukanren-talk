def unify (term1, term2, subst_map):
    if subst_map is None:
        return None
    term1 = resolve(term1, subst_map)
    term2 = resolve(term2, subst_map)
    if is_var(term1) and is_var(term2) and term1 == term2:
        return subst_map
    elif is_var(term1):
        return extend (subst_map, term1, term2)
    elif is_var(term2):
        return extend(subst_map, term2, term1)
    elif is_cons(term1) and is_cons(term2):
        subst_map = unify(head(term1), head(term2), subst_map)
        return unify(tail(term1), tail(term2), subst_map)
    elif term1 == term2:
        return subst_map

####
subst_map = {var(1): var(2), var(2): 3}
unify (var(1), 3, subst_map)
unify (var(1), 4, subst_map)
