######################################################################################
#                                     Rules                                          #
######################################################################################


## import dependencies
from relation import Relation
from typing import Set
from model import *

class Rule(object):
    """class for rules"""
    def __init__(self, head:Relation, body:Set[Relation]):
        """
        head: Relation
        body: set of relations
        """
        self.head = head
        self.body = body

    def get_head_variables(self):
        """retun the variables of the head of the rule"""
        return set([var for var, _ in self.head])

    def __len__(self):
        """return the number of elements in the body of the rule"""
        return len(self.body)

    def __repr__(self):
        """represent a rule by its head & body"""
        head = ', '.join([ele.__repr__() for ele in self.head.relation])
        body = ', '.join([ele.__repr__() for ele in self.body.relation])
        return f"{head} :- {body}"


## test

if __name__ == "__main__":

    ## create variables
    x = Variable('x')
    y = Variable('y')

    ## create rule' head & body
    head = Relation()
    head.add((Acts(x, y)))
    body = Relation()
    body.add(Actor(x))
    body.add(Film(y))

    ## create the rule
    rule = Rule(head, body)

    print(rule)