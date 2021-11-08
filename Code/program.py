## Evaluation of Non-recursive datalog

"""
TODO
====
    1. Design an interface for relation.
    2. Impliment relations without indexes.
    3. Impliment rule evaluation.
    4. Impliment program evaluation.
    5. Impliment relations with indexes.
"""

from typing import List
from rule import Rule
from relation import Relation
from model import *

class Program(object):

    def __init__(self, rules:List[Rule]):
        self.rules = rules

    def __repr__(self):
        return "\n".join(rule.__repr__() for rule in self.rules)




x = Variable('x')
y = Variable('y')


head = Relation()
head.add((Acts(x, y)))

body = Relation()

body.add(Actor(x))
body.add(Film(y))

rule = Rule(head, body)
print(rule)
