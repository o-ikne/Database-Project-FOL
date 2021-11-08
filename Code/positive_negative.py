##################################################################################
#                       Positive & Negative Visitors                             #
##################################################################################

## import dependencies
from model import *
from visitor import VisitUnaryExpression


##
class Positive(VisitUnaryExpression):
    """
    Class for Positive visitor.
    The Positive can run visitor operations over any set of elements without
    figuring out their concrete classes. The accept operation directs a call to
    the appropriate operation in the visitor object.
    """

    def __init__(self):
        ## initiate instances
        pass

    def visitVariable(self, var:Variable):
        """visitor visiting variable"""
        return var

    def visitEqual(self, phi:Equal):
        """visitor visiting Equality"""
        return phi

    def visitAnd(self, phi:And):
        """visitor visiting Conjunction"""
        left = phi.leftExpression.accept(self)
        right = phi.rightExpression.accept(self)
        return And(left, right)

    def visitOr(self, phi:Or):
        """visitor visiting Disjunction"""
        left = phi.leftExpression.accept(self)
        right = phi.rightExpression.accept(self)
        return Or(left, right)

    def visitNot(self, phi:Not):
        """visitor visiting Negation"""
        expr = phi.expression.accept(Negative())
        return expr

    def visitExists(self, phi:Exists):
        """visitor visiting Exists"""
        expr = phi.predicate.accept(self)
        var = phi.variable
        return Exists(var, expr)

    def visitForall(self, phi:Forall):
        """visitor visiting Forall"""
        expr = phi.predicate.accept(Negative())
        var = phi.variable
        return Not(Exists(var, expr))

    def visitActor(self, actor:Actor):
        """visitor visiting actors"""
        return actor

    def visitArtist(self, artist:Artist):
        """visitor visiting artists"""
        return artist

    def visitDirector(self, director:Director):
        """visitor visiting film directors"""
        return director

    def visitFilm(self, film:Film):
        """visitor visiting movies"""
        return film

    def visitActs(self, acts:Acts):
        """visitor visiting acts"""
        return acts

    def visitDirects(self, directs:Directs):
        """visitor visiting directs"""
        return directs
    

class Negative(VisitUnaryExpression):

    """
    The Negative can run visitor operations over any set of elements without
    figuring out their concrete classes. The accept operation directs a call to
    the appropriate operation in the visitor object.
    """

    def __init__(self):
        ## initiate instances
        pass

    def visitVariable(self, var:Variable):
        """visitor visiting variable"""
        return var

    def visitAnd(self, phi:And):
        """visitor visiting Conjunction"""
        left = phi.leftExpression.accept(self)
        right = phi.rightExpression.accept(self)
        return Or(left, right)

    def visitOr(self, phi:Or):
        """visitor visiting Disjunction"""
        left = phi.leftExpression.accept(self)
        right = phi.rightExpression.accept(self)
        return And(left, right)

    def visitNot(self, phi:Not):
        """visitor visiting Negation"""
        expr = phi.expression.accept(Negative())
        return expr.accept(Positive())

    def visitExists(self, phi:Exists):
        """visitor visiting Exists"""
        expr = phi.predicate.accept(Positive())
        var = phi.variable
        return Not(Exists(var, expr))

    def visitForall(self, phi:Forall):
        """visitor visiting Forall"""
        expr = phi.predicate.accept(self)
        var = phi.variable
        return Exists(var, expr)

    def visitActor(self, actor:Actor):
        """visitor visiting actors"""
        return actor

    def visitArtist(self, artist:Artist):
        """visitor visiting artists"""
        return artist

    def visitDirector(self, director:Director):
        """visitor visiting film directors"""
        return director

    def visitFilm(self, film:Film):
        """visitor visiting movies"""
        return film

    def visitActs(self, acts:Acts):
        """visitor visiting acts"""
        return acts

    def visitDirects(self, directs:Directs):
        """visitor visiting directs"""
        return directs
    

## Proposal testing: we will test our proposal on some simple queries !

if __name__ == "__main__":

    ## create Postive & Negative instances
    Pos = Positive()
    Neg = Negative()

    ## create variables
    x = Variable('x')
    y = Variable('y')

    ## simple queries to set our proposal
    query_0 = Exists(x, And(Actor(x), Artist(x)))
    query_1 = Forall(x, Or(Not(Artist(x)), Or(And(Artist(x), Actor(x)), And(Artist(x), Director(x)))))
    query_2 = Forall(x, Or(Not(Actor(x)), Exists(y, And(Film(y), Acts(x, y)))))
    query_3 = Forall(x, Or(Not(Director(x)), Exists(y, And(Film(y), Directs(x, y)))))
    
    queries = [query_0, query_1, query_2, query_3]
    
    ## test queries
    for e, query in enumerate(queries):
        print(f"\nQuery {e}: {query}")

        pos = query.accept(Pos)
        neg = query.accept(Neg)

        print(f"\t-Positive: {pos}")
        print(f"\t-Negative: {neg}")