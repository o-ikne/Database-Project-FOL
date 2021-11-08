######################################################################################################################
#                                                     Relations                                                      #
######################################################################################################################

"""
How to represent a relation ?
=============================
So as to improve the effeciency of joins, we want to use indexes.
Suppose we work with an n-array relation, we can construct n indexes for this relation  (1 index for each dimension).
In python, we can use dictionnaries to represent indexes. 
The index of the i-th dimension being a dictionnary where keys are the values in the i-th dimension of the relation.
A key is the associated to the set of tuples which have them in the i-th dimension.

Example:
========
Consider the following relation:
    {(1, 2), (2, 4), (1, 6), (5, 2), (1, 4)}

Its index in the first dimension is:
    1 -> {(1, 2), (1, 6), (1, 4)}
    2 -> {(2, 4)}
    5 -> {(5, 2)}

Its index in the second dimension:
    2 -> {(1, 2), (5, 2)}
    4 -> {(2, 4), (1, 4)}
    6 -> {(1, 6)}
"""

## import dependencies
from copy import deepcopy
from model import *


##
class Relation:

    def __init__(self):
        """
        relation: set of tuples
        """
        self.relation = set()

    def add(self, element:tuple)->None: 
        """add an element to the relation
        element: <tuple>: the element to add to the relation
        """
        self.relation.add(element)
    
    def remove(self, element:tuple)->None:
        """remove an element from the relation
           element: <tuple>: the lement to remove from the relation
        """
        self.relation.remove(element)

    def union(self, other):
        """return the union of this relation and other relation
           other: <Relation>
        """
        self.relation.update(other.relation)
        return self

    def copy(self):
        """return a copy of the relation"""
        return deepcopy(self)

    def construct_indexes(self, dimension:int=0)->dict:
        indexes = {tup[dimension]:set() for tup in self.relation}
        for tup in self.relation:
            indexes[tup[dimension]].add(tup)
        return indexes

    def __len__(self)->int:
        """return the number of conditions in the relation"""
        return len(self.relation)

    def __repr__(self)->str:
        """repesent a relation by its elements"""
        return str(self.relation)



## test

if __name__ == "__main__":

    ## tuples
    tups = {(1, 2), (2, 4), (1, 6), (5, 2), (1, 4)}

    ## create a relation
    relation = Relation()
    for tup in tups:
        relation.add(tup)

    print(f"relation: {relation}")

    ## indexes on 1st-dimension
    indexes = relation.construct_indexes(dimension=0)
    print("Its indexes in the first dimension:\n", indexes)

    ## indexes on 2nd-dimension
    indexes = relation.construct_indexes(dimension=1)
    print("Its indexes in the second dimension:\n", indexes, end='\n\n')


    ## 
    ## create variables
    x = Variable('x')
    y = Variable('y')

    ## predicates
    p = Not(Actor(x))
    q = And(Actor(x), And(Film(y), Acts(x, y)))
    print(f"p(x):-{p}")
    print(f"q(x, y):-{q}")

    ## associate numbers to predicates
    f = dict()
    f['p'] = 4
    f['q'] = 5
    f['actor'] = 3
    f['film'] = 2
    f['acts'] = 1
    print(f"f={f}")