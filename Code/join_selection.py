#####################################################################
#       Join via stream fusion | Cartesien product | Selection      #
#####################################################################



def cartesien_product(t1, t2):
    """return cartesien product of t1 and t2"""
    res = set()
    for e1 in t1:
        for e2 in t2:
            res = res.union({(e1, e2)})
    
    return res


def select(t, property):
    """it's kind of a filter filter(property, t1)"""
    res = set()
    for e in t:
        if property(e):
            res = res.union({e})
    
    return res


def join(t1, t2, property):
    """join"""
    return select(cartesien_product(t1, t2), property)


"""Direct way"""

def inlined_join(t1, t2, property):
    """inlined join"""
    res = set()
    for e1 in t1:
        for e2 in t2:
            res = res.union({(e1, e2)})

    res0 = set()
    for e in res:
        if property(e):
            res0 = res0.union(e)
    
    return res0


def fused_join(t1, t2, property):
    """fusion join"""
    res = set()
    for e1 in t1:
        for e2 in t2:
            e = (e1, e2) # this is not what we want /!\ ==> Suppose we want to compute |X| 
                         #                                                            /   \
                         #                                                      a(x, y)    b(y, z)
                         # If we produce pairs of elements coming from a and coming from b,
                         # we do not obtain what we are exepecting ! i.e., tuples(e, f, g) so that (e, f) in a and (f, g) in b.
            if property(e):
                res = res.union(e)

    return res



def new_fusion_join(t1, t2, property):
    ...